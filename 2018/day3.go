package main

import (
	"fmt"
	"strconv"
	"strings"
)
type point struct {
	x, y int
}

type rectangle struct {
	a, b, c, d point
}


func day3_1(data []string) int{
	
	for _, line := range data {
		lineArr := strings.Split(line, ":")
		fmt.Println(lineArr[0], lineArr[1])

		metaData := strings.Split(lineArr[0], " ")
		dimensions := strings.Split(metaData[2], ",")
		size := strings.Split(lineArr[1], "x")
		// describes the fabric required
		x, _ := strconv.Atoi(dimensions[0])
		y, _ := strconv.Atoi(dimensions[1])
		width, _ := strconv.Atoi(size[0])
		height, _ := strconv.Atoi(size[1])

		a := point{x:x, y:y}
		b := point{x:x+width, y:y}
		c := point{x:x+width, y:y+height }
		d := point{x:x, y:y+height}
		rect := rectangle{a, b, c, d}

	}
	return 0
}


func main() {
	fmt.Println("day three")
	data, err := ReadLines("./data/day_3.txt")
	if err!= nil {
		panic(err)
	}
	day3_1(data)
}
