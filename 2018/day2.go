package main

import (
	"fmt"
	"strings"
)


func day2_1(data []string) int {
	two := 0
	three := 0

	for _, line := range data {
		duplicates := make([]int, 0)
		visited := make([]string, 0)

		lineArr := strings.Split(line, "")

		for i, character := range lineArr {

			nubOccurrences := 1
			if !containsString(character, visited) {
				nubOccurrences = countOccurrences(lineArr[i+1:], character)
			}
			visited = append(visited, character)
			duplicates = append(duplicates, nubOccurrences)
		}

		if ContainsInt(2, duplicates) {
			two++
		}

		if ContainsInt(3, duplicates) {
			three++
		}
	}
	return two * three
}


func day2_2(data []string) string {
	for i, line := range data {
		for _, nextLine := range data[i+1:] {
			isOffByOne, indices := OffByOneMatch(line, nextLine)
			if isOffByOne{
				s1Arr := strings.Split(line, "")
				index:= indices[0]
				result:= append(s1Arr[:index], s1Arr[index+1:]...)
				return strings.Join(result, "")
			}
		}
	}
	return ""
}

// helper

func OffByOneMatch(s1 string, s2 string) (bool, []int) {
	s1Arr := strings.Split(s1, "")
	s2Arr := strings.Split(s2, "")

	differences := make([]int, 0)
	for i, _ := range s1Arr {
		if s1Arr[i] != s2Arr[i] {
			differences = append(differences, i)
		}
	}
	if len(differences) > 1 {
		return false, differences
	}
	return true, differences
}

func countOccurrences(data []string, element string) int {
	count := 1
	for _, value := range data {
		if element == value {
			count ++
		}
	}
	return count
}

func main() {
	fmt.Println("day two")
	data, err := ReadLines("./data/2_1.txt")
	if err!= nil {
		panic(err)
	}
	_part1 := day2_1(data)
	_part2 := day2_2(data)

	fmt.Println(_part1)
	fmt.Println(_part2)

}