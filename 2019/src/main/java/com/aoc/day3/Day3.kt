package com.aoc.day3

import java.lang.IllegalArgumentException
import kotlin.math.absoluteValue
import kotlin.math.roundToInt

data class Coord(val x: Int, val y: Int) {

    fun left(length: Int): Coord {
        return Coord(this.x - length, this.y)
    }

    fun right(length: Int): Coord {
        return Coord(this.x + length, this.y)
    }

    fun up(length: Int): Coord {
        return Coord(this.x, this.y + length)
    }

    fun down(length: Int): Coord {
        return Coord(this.x, this.y - length)
    }

    fun delta(other: Coord): Coord {
        return Coord(other.x - this.x, other.y - this.y)
    }

    fun manhattanDistance(): Int {
        return x.absoluteValue + y.absoluteValue
    }

    companion object {
        val zero = Coord(0, 0)
    }
}

fun String.toCoordTransform(): (Coord) -> Coord {
    return {
        when (this[0]) {
            'U' -> it::up
            'D' -> it::down
            'L' -> it::left
            'R' -> it::right
            else -> throw IllegalArgumentException("Illegal coordinate transform $this")
        }.invoke(this.removeRange(0, 1).toInt())
    }
}

fun String.toWireSegments(): List<WireSegment> {
    return this.split(",")
            .map { it.toCoordTransform() }
            .foldMap(Coord.zero)
            .zipWithNext()
            .map { (first, second) -> WireSegment(first, second) }
}

fun findClosestCrossing(red: List<WireSegment>, green: List<WireSegment>): Coord? {
    return red.cartesianProduct(green)
            .mapNotNull { (first, second) -> first.intersection(second) }
            .filter { it != Coord.zero }
            .minBy { it.manhattanDistance() }
}

fun <U, V> List<U>.cartesianProduct(other: List<V>): List<Pair<U, V>> {
    return this.flatMap { u -> other.map { v -> Pair(u, v) } }
}

fun <T> Iterable<(T) -> T>.foldMap(initial: T): Iterable<T> {
    return this.fold(mutableListOf(initial)) { acc, fnc -> acc.also { it.add((fnc)(acc.last())) } }
}

data class WireSegment(val start: Coord, val end: Coord) {

    fun delta(): Coord {
        return start.delta(end)
    }

    fun length(): Int {
        return start.delta(end).manhattanDistance()
    }

    fun intersection(other: WireSegment): Coord? {
        val u = this.delta()
        val v = other.delta()

        val divisor = v.y * u.x - v.x * u.y

        if (divisor == 0)
            return null

        val d = this.start.delta(other.start)

        val t = (v.y * d.x - v.x * d.y).toDouble() / divisor.toDouble()
        val w = (u.y * d.x - u.x * d.y).toDouble() / divisor.toDouble()

        return if ((t >= 0 && Coord((u.x * t).roundToInt(), (u.y * t).roundToInt()).manhattanDistance() <= this.length())
                && (w >= 0 && Coord((v.x * w).roundToInt(), (v.y * w).roundToInt()).manhattanDistance() <= other.length()))
            Coord((u.x * t + start.x).roundToInt(), (u.y * t + start.y).roundToInt())
        else
            null
    }
}