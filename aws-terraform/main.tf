#明示的にproviderとリージョンを定義しておく
provider aws {
  region = "ap-northeast-1"
}

#インスタンスのタイプを変数として定義
variable "example_instance_type" {
  default = "t2.micro"
}

# EC2インスタンスのセキュリティグループを定義する
resource "aws_security_group" "example_ec2_sg" {
  name = "example-ec2-sg"

  #httpのインバウントのSG
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  #sshのインバウンドのSG
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  #アウトバウンドのSG
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# EC2インスタンスを定義する
# resource <リソースの種類> <リソースの名前>でリソースを定義できる
resource "aws_instance" "example" {
  # centos7のAMI ID(これは決まってる)
  ami = "ami-045f38c93733dd48d"

  # さっき定義したインスタンスのタイプの変数を参照している
  instance_type = var.example_instance_type

  # resource "aws_key_pair" "example"で定義した公開鍵を参照する
  key_name = aws_key_pair.example.id

  # EC2に定義したセキュリティグループを追加する
  vpc_security_group_ids = [aws_security_group.example_ec2_sg.id]

  #インスタンス内で実行したいスクリプトを定義できる
  user_data = file("./user_data.sh")

  # インスタンスに名前を付ける
  tags = {
    Name = "example"
  }
}

# terraformでEC2インスタンスに公開鍵を登録するために公開鍵のファイルを指定する
resource "aws_key_pair" "example" {
  key_name   = "example"
  public_key = file("./.ssh/id_rsa.pub") # 先程`ssh-keygen`コマンドで作成した公開鍵を指定
}

# applyを実行したときに標準出力で出力したい情報を定義する
output "example_public_dns" {
  # type.name.attribute のように書く
  value = aws_instance.example.public_dns
}