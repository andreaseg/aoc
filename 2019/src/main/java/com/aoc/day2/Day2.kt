package com.aoc.day2

class IntcodeVM(instructions: List<Int>) {
    private val store: MutableList<Int> = instructions.toMutableList()
    private var pc: Int = 0;

    fun interpret() {
        pc = 0
        while (pc / 4 < store.size / 4) {
            val currentInstruction = store[pc]
            when (currentInstruction) {
                1 -> add()
                2 -> mul()
                99 -> return
            }
            pc += 4
        }
    }

    fun printStore() {
        store.chunked(4)
                .map { it.joinToString(", ")}
                .forEach(::println)
    }

    fun readStore(): List<Int> {
        return store.toList()
    }

    private fun ternaryLoad(): Triple<Int, Int, Int> {
        return Triple(store[pc + 1], store[pc + 2], store[pc + 3])
    }

    private fun add() {
        val (left, right, pos) = ternaryLoad()
        store[pos] = store[left] + store[right]
    }

    private fun mul() {
        val (left, right, pos) = ternaryLoad()
        store[pos] = store[left] * store[right]
    }
}