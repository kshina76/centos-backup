package util

func TestFunc() {
	testBody := `
		{{define "test"}}
			{{.Name}}
		{{end}}
	`
	testParams := make(map[string]string)
	test, _ := template.New("test").Parse(testBody)
	testParams["Email"] = request.PostFormValue("email")
	test.Execute(writer, testParams)
}