package main

import (
	"fmt"
	"strconv"
)




func day1_1(data []string) (int) {
	result := 0

	for _, element := range data {
		i, _ := strconv.Atoi(element)
		result = result + i
	}

	return result
}

func day1_2(data []string, seen []int, result int) int {

	for _, element := range data {
		i, _  := strconv.Atoi(element)
		seen = append(seen, result)
		result = result + i

		if ContainsInt(result, seen) {
			return result
		}
	}
	return day1_2(data, seen, result)
}




func main() {
	fmt.Println("day one")
	data, err := ReadLines("./data/1_1.txt")
	if err!= nil {
		panic(err)
	}
	_part1 := day1_1(data)
	_part2 := day1_2(data, make([]int, 100), 0 )

	fmt.Println(_part1)
	fmt.Println(_part2)
}