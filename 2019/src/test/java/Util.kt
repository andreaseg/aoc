package com.aoc

fun readPartOne(day: Int): List<String> {
    return object {}.javaClass.getResource("/day$day/part1.input").readText().lines()
}

fun readPartTwo(day: Int): List<String> {
    return object {}.javaClass.getResource("/day$day/part2.input").readText().lines()
}