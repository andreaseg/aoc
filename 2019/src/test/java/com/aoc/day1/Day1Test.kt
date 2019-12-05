package com.aoc.day1

import com.aoc.readPartOne
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test

class Day1Test {

    @Test
    fun `part 1`() {
        val result = readPartOne(1)
                .map(String::toFuel)
                .fuelToLaunch()

        println("Day 1 part 1. The required amount of fuel is $result")
    }

    @Test
    fun `part 2`() {
        val result = readPartOne(1)
                .map(String::toFuel)
                .fuelToLaunchRecursive()

        println("Day 1 part 2. The required amount of fuel is $result")
    }

    @Test
    fun `part2 example`() {
        assertEquals(2, Fuel(14).toLaunchModuleRecursive().mass)
        assertEquals(966, Fuel(1969).toLaunchModuleRecursive().mass)
        assertEquals(50346, Fuel(100756).toLaunchModuleRecursive().mass)
    }

}

