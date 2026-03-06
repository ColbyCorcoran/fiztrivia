import TipKit

// MARK: - Game Mode Tip
struct GameModeTip: Tip {
    var title: Text {
        Text("Change How You Play")
    }
    var message: Text? {
        Text("Tap the Mode badge to quickly switch between Multi-Category, Single Category, and Single Topic modes.")
    }
    var image: Image? {
        Image(systemName: "circle.grid.cross.left.filled")
    }
}

// MARK: - Expansion Pack Tip
struct ExpansionPackTip: Tip {
    var title: Text {
        Text("Add More Questions")
    }
    var message: Text? {
        Text("Expand your trivia library with themed packs — Harry Potter, Pokémon, Star Wars, and more. Tap to browse.")
    }
    var image: Image? {
        Image(systemName: "rectangle.stack.badge.plus")
    }
}

// MARK: - Phobia Filter Tip
struct PhobiaFilterTip: Tip {
    var title: Text {
        Text("Filter Out Topics You Dislike")
    }
    var message: Text? {
        Text("Not a fan of certain topics? Phobia Filters let you exclude questions about spiders, snakes, heights, and more.")
    }
    var image: Image? {
        Image(systemName: "eye.slash")
    }
}

// MARK: - Difficulty Tip
struct DifficultyTip: Tip {
    var title: Text {
        Text("Find Your Perfect Challenge")
    }
    var message: Text? {
        Text("Casual shows only easy questions. Difficult focuses on medium and hard. Normal includes everything.")
    }
    var image: Image? {
        Image(systemName: "speedometer")
    }
}
