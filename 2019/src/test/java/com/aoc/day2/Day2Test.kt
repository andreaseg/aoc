package com.aoc.com.aoc.day2

import com.aoc.day2.IntcodeVM
import com.aoc.readPartOne
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Assertions.assertNotEquals
import org.junit.jupiter.api.Test

class Day2Test {

    @Test
    fun `part 1 example`() {
        val in1 = listOf(1, 0, 0, 0, 99)
        val out1 = listOf(2, 0, 0, 0, 99)

        val in2 = listOf(2, 3, 0, 3, 99)
        val out2 = listOf(2, 3, 0, 6, 99)

        val in3 = listOf(2, 4, 4, 5, 99, 0)
        val out3 = listOf(2, 4, 4, 5, 99, 9801)

        val in4 = listOf(1, 1, 1, 4, 99, 5, 6, 0, 99)
        val out4 = listOf(30, 1, 1, 4, 2, 5, 6, 0, 99)

        assertEquals(out1, IntcodeVM(in1).also { it.interpret() }.readStore())
        assertEquals(out2, IntcodeVM(in2).also { it.interpret() }.readStore())
        assertEquals(out3, IntcodeVM(in3).also { it.interpret() }.readStore())
        assertEquals(out4, IntcodeVM(in4).also { it.interpret() }.readStore())

    }

    @Test
    fun `part 1`() {
        val input = readPartOne(2)[0]
                .split(',')
                .map(String::toInt)

        val result = IntcodeVM(input.toMutableList().also {
            it[1] = 12
            it[2] = 2
        })
                .also {it.interpret()}
                .readStore()[0]


        assertNotEquals(1870666, result)

        println("Day 1 part 1. The value in the first slot is $result")
    }

    @Test
    fun `part 2`() {
        val target = 19690720

        val input = readPartOne(2)[0]
                .split(',')
                .map(String::toInt)

        for (noun in 0..100) {
            for (verb in 0..100) {
                val result = IntcodeVM(input.toMutableList().also {
                    it[1] = noun
                    it[2] = verb
                })
                        .also {it.interpret()}
                        .readStore()[0]

                if (result == target) {
                    val answer = 100 * noun + verb
                    println("Day 1 part 2. The answer is $answer")
                    return
                }
            }
        }
    }
}