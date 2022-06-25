package main

import (
	"fmt"
	"net"
)

func Is_valid_ip(ip string) bool {
	if r := net.ParseIP(ip); r == nil {
		return false
	}
	return true
}

func main() {
	fmt.Println(Is_valid_ip("1.2.2.2"))
	fmt.Println(Is_valid_ip("1.2.3.4"))
	fmt.Println(Is_valid_ip("123.45.67.89"))

	fmt.Println(Is_valid_ip("1.2.3"))
	fmt.Println(Is_valid_ip("1.2.3.4.5"))
	fmt.Println(Is_valid_ip("123.456.78.90"))
	fmt.Println(Is_valid_ip("123.045.067.089"))
}
