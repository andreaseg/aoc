package com.aoc.com.aoc.day3

import com.aoc.day3.Coord
import com.aoc.day3.WireSegment
import com.aoc.day3.findClosestCrossing
import com.aoc.day3.toWireSegments
import com.aoc.readPartOne
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test

class Day3Test {

    @Test
    fun `Day 3 examples`() {

        findDistance("R8,U5,L5,D3", "U7,R6,D4,L4", 6)

        findDistance("R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83", 159)

        findDistance("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7", 135)

    }

    @Test
    fun `Day 3`() {
        val input = readPartOne(3)

        val closestCrossing = findClosestCrossing(input[0].toWireSegments(), input[1].toWireSegments())

        println("Point of closest crossed wires are $closestCrossing with a distance of ${closestCrossing?.manhattanDistance()}")
    }

    private fun findDistance(redWire: String, greenWire: String, expected: Int?): Int? {
        val redWireSegments = redWire.toWireSegments()
        val greenWireSegments = greenWire.toWireSegments()
        val distance = findClosestCrossing(redWireSegments, greenWireSegments)?.manhattanDistance()

        if (expected != null && distance != expected) {

            println("Red wire")
            redWireSegments.forEach { println(" (${it.start.x}, ${it.start.y}) --> (${it.end.x}, ${it.end.y})") }

            println("Green wire")
            greenWireSegments.forEach { println(" (${it.start.x}, ${it.start.y}) --> (${it.end.x}, ${it.end.y})") }

            throw AssertionError("Expected $expected, actual $distance")
        }

        return distance
    }

    @Test
    fun `closest crossing`() {
        val crossing = findClosestCrossing(listOf(WireSegment(Coord(-2, -1), Coord(2, -1))), listOf(WireSegment(Coord(1, 2), Coord(1, -2))))
        assertEquals(Coord(1, -1), crossing)
    }
}