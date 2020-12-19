#!/bin/sh

sass ./static/sass/$1.scss:./static/css/$1.css
go run main.go