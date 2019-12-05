package com.aoc.day1

data class Fuel(val mass: Int) {

    operator fun plus(other: Fuel): Fuel {
        return Fuel(this.mass + other.mass)
    }

    operator fun minus(other: Int): Fuel {
        return Fuel(this.mass - other)
    }

    operator fun div(other: Int): Fuel {
        return Fuel(this.mass / other)
    }

    operator fun compareTo(other: Int): Int {
        return this.mass.compareTo(other)
    }

    fun toLaunchModule(): Fuel {
        return this / 3 - 2
    }

    fun toLaunchModuleRecursive(): Fuel {
        val fuelToLaunchThisFuel = this.toLaunchModule()

        return if (fuelToLaunchThisFuel > 0)
            fuelToLaunchThisFuel + fuelToLaunchThisFuel.toLaunchModuleRecursive()
        else
            Fuel(0)
    }
}

fun String.toFuel(): Fuel {
    return Fuel(this.toInt())
}

fun List<Fuel>.fuelToLaunch(): Fuel {
    return Fuel(this.map(Fuel::toLaunchModule).sumBy(Fuel::mass))
}

fun List<Fuel>.fuelToLaunchRecursive(): Fuel {
    return Fuel(this.map(Fuel::toLaunchModuleRecursive).sumBy(Fuel::mass))
}