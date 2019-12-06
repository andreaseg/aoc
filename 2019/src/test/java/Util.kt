package com.aoc

import java.io.FileNotFoundException
import java.net.URL

fun readPartOne(day: Int): List<String> {
    return readResourceAsLines("/day$day/part1.input")
}

fun readPartTwo(day: Int): List<String> {
    return readResourceAsLines("/day$day/part2.input")
}

private fun readResourceAsLines(filename: String): List<String> {
    val resource: URL? = object {}.javaClass.getResource(filename)
    if (resource != null)
        return resource.readText().lines()
    else
        throw FileNotFoundException("Resource $filename could not be read")
}