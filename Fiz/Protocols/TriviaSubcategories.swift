//
//  TriviaSubcategories.swift
//  Fiz
//
//  Extracted from TriviaModels.swift during code review refactor
//

import Foundation

// MARK: - Subcategory Protocol
protocol TriviaSubcategory {
    var name: String { get }
    var icon: String { get }
    var color: String { get }
}

// MARK: - Entertainment Subcategories
struct EntertainmentSubcategory: TriviaSubcategory {
    let name: String
    let icon: String
    let color: String

    static let animation = EntertainmentSubcategory(name: "Animation", icon: "film.stack.fill", color: "#F7B500")
    static let sciFiFantasy = EntertainmentSubcategory(name: "Sci-Fi/Fantasy", icon: "sparkles", color: "#FF7F0F")
    static let actionAdventure = EntertainmentSubcategory(name: "Action/Adventure", icon: "figure.run", color: "#8E44AD")
    static let dramaComedy = EntertainmentSubcategory(name: "Drama/Comedy", icon: "theatermasks.fill", color: "#3498DB")

    static let all: [EntertainmentSubcategory] = [animation, sciFiFantasy, actionAdventure, dramaComedy]
}

// MARK: - Sports Subcategories
struct SportsSubcategory: TriviaSubcategory {
    let name: String
    let icon: String
    let color: String

    static let teamSports = SportsSubcategory(name: "Team Sports", icon: "figure.basketball", color: "#F7B500")
    static let individualSports = SportsSubcategory(name: "Individual Sports", icon: "figure.tennis", color: "#FF7F0F")
    static let internationalCompetition = SportsSubcategory(name: "International Competition", icon: "medal.fill", color: "#8E44AD")
    static let extremeActionSports = SportsSubcategory(name: "Extreme & Action Sports", icon: "figure.snowboarding", color: "#3498DB")
    static let sportsHistoryRecords = SportsSubcategory(name: "Sports History & Records", icon: "trophy.fill", color: "#1ABC9C")
    static let athletesBiography = SportsSubcategory(name: "Athletes & Biography", icon: "person.2.fill", color: "#2ECC71")

    static let all: [SportsSubcategory] = [teamSports, individualSports, internationalCompetition, extremeActionSports, sportsHistoryRecords, athletesBiography]
}

// MARK: - Bible Subcategories
struct BibleSubcategory: TriviaSubcategory {
    let name: String
    let icon: String
    let color: String

    static let bibleTrivia = BibleSubcategory(name: "Bible Trivia", icon: "text.book.closed.fill", color: "#F7B500")
    static let biblicalHistory = BibleSubcategory(name: "Biblical History", icon: "clock.arrow.circlepath", color: "#FF7F0F")
    static let biblicalTheology = BibleSubcategory(name: "Biblical Theology", icon: "text.magnifyingglass", color: "#8E44AD")
    static let bibleLanguages = BibleSubcategory(name: "Bible Languages", icon: "pencil.and.scribble", color: "#3498DB")

    static let all: [BibleSubcategory] = [bibleTrivia, biblicalHistory, biblicalTheology, bibleLanguages]
}

// MARK: - History Subcategories
struct HistorySubcategory: TriviaSubcategory {
    let name: String
    let icon: String
    let color: String

    static let modernHistory = HistorySubcategory(name: "Modern History", icon: "building.fill", color: "#F7B500")
    static let ancientHistory = HistorySubcategory(name: "Ancient History", icon: "building.columns.fill", color: "#FF7F0F")
    static let medievalHistory = HistorySubcategory(name: "Medieval History", icon: "shield.lefthalf.filled", color: "#8E44AD")
    static let churchHistory = HistorySubcategory(name: "Church History", icon: "text.book.closed.fill", color: "#3498DB")

    static let all: [HistorySubcategory] = [modernHistory, ancientHistory, medievalHistory, churchHistory]
}

// MARK: - Science Subcategories
struct ScienceSubcategory: TriviaSubcategory {
    let name: String
    let icon: String
    let color: String

    static let biology = ScienceSubcategory(name: "Biology", icon: "leaf.fill", color: "#F7B500")
    static let chemistry = ScienceSubcategory(name: "Chemistry", icon: "flask.fill", color: "#FF7F0F")
    static let physics = ScienceSubcategory(name: "Physics", icon: "atom", color: "#8E44AD")
    static let astronomy = ScienceSubcategory(name: "Astronomy", icon: "moon.stars.fill", color: "#3498DB")

    static let all: [ScienceSubcategory] = [biology, chemistry, physics, astronomy]
}

// MARK: - Nature Subcategories
struct NatureSubcategory: TriviaSubcategory {
    let name: String
    let icon: String
    let color: String

    static let trees = NatureSubcategory(name: "Trees", icon: "tree.fill", color: "#F7B500")
    static let weather = NatureSubcategory(name: "Weather", icon: "cloud.sun.fill", color: "#FF7F0F")
    static let plantsFlowers = NatureSubcategory(name: "Plants & Flowers", icon: "leaf.fill", color: "#8E44AD")
    static let animalsWildlife = NatureSubcategory(name: "Animals & Wildlife", icon: "pawprint.fill", color: "#3498DB")
    static let oceansMarineLife = NatureSubcategory(name: "Oceans & Marine Life", icon: "water.waves", color: "#1ABC9C")

    static let all: [NatureSubcategory] = [trees, weather, plantsFlowers, animalsWildlife, oceansMarineLife]
}

// MARK: - Food Subcategories
struct FoodSubcategory: TriviaSubcategory {
    let name: String
    let icon: String
    let color: String

    static let ingredients = FoodSubcategory(name: "Ingredients", icon: "carrot.fill", color: "#F7B500")
    static let bakingDesserts = FoodSubcategory(name: "Baking & Desserts", icon: "birthday.cake.fill", color: "#FF7F0F")
    static let cooking = FoodSubcategory(name: "Cooking", icon: "cooktop.fill", color: "#8E44AD")
    static let foodHistory = FoodSubcategory(name: "Food History", icon: "clock.arrow.circlepath", color: "#3498DB")
    static let dishesCuisines = FoodSubcategory(name: "Dishes & Cuisines", icon: "fork.knife", color: "#1ABC9C")
    static let beverages = FoodSubcategory(name: "Beverages", icon: "cup.and.saucer.fill", color: "#2ECC71")

    static let all: [FoodSubcategory] = [ingredients, bakingDesserts, cooking, foodHistory, dishesCuisines, beverages]
}

// MARK: - Literature Subcategories
struct LiteratureSubcategory: TriviaSubcategory {
    let name: String
    let icon: String
    let color: String

    static let fantasyLiterature = LiteratureSubcategory(name: "Fantasy Literature", icon: "wand.and.stars", color: "#F7B500")
    static let classicLiterature = LiteratureSubcategory(name: "Classic Literature", icon: "book.closed.fill", color: "#FF7F0F")
    static let modernFiction = LiteratureSubcategory(name: "Modern Fiction", icon: "book.pages.fill", color: "#8E44AD")
    static let poetry = LiteratureSubcategory(name: "Poetry", icon: "text.alignleft", color: "#3498DB")
    static let childrensBooks = LiteratureSubcategory(name: "Children's Books", icon: "figure.and.child.holdinghands", color: "#1ABC9C")
    static let authorsBiography = LiteratureSubcategory(name: "Authors & Biography", icon: "person.text.rectangle.fill", color: "#2ECC71")

    static let all: [LiteratureSubcategory] = [fantasyLiterature, classicLiterature, modernFiction, poetry, childrensBooks, authorsBiography]
}

// MARK: - Music Subcategories
struct MusicSubcategory: TriviaSubcategory {
    let name: String
    let icon: String
    let color: String

    static let historyEras = MusicSubcategory(name: "History & Eras", icon: "clock.arrow.circlepath", color: "#F7B500")
    static let musiciansBands = MusicSubcategory(name: "Musicians & Bands", icon: "guitars.fill", color: "#FF7F0F")
    static let awardsRecords = MusicSubcategory(name: "Awards & Records", icon: "trophy.fill", color: "#8E44AD")
    static let instrumentsTheory = MusicSubcategory(name: "Instruments & Theory", icon: "music.quarternote.3", color: "#3498DB")
    static let filmTV = MusicSubcategory(name: "Film & TV", icon: "music.note.tv.fill", color: "#1ABC9C")

    static let all: [MusicSubcategory] = [historyEras, musiciansBands, awardsRecords, instrumentsTheory, filmTV]
}

// MARK: - Technology Subcategories
struct TechnologySubcategory: TriviaSubcategory {
    let name: String
    let icon: String
    let color: String

    static let videoGames = TechnologySubcategory(name: "Video Games", icon: "gamecontroller.fill", color: "#F7B500")
    static let computersSoftware = TechnologySubcategory(name: "Computers & Software", icon: "desktopcomputer", color: "#FF7F0F")
    static let internetSocialMedia = TechnologySubcategory(name: "Internet & Social Media", icon: "network", color: "#8E44AD")
    static let techCompanies = TechnologySubcategory(name: "Tech Companies", icon: "building.2.fill", color: "#3498DB")
    static let inventions = TechnologySubcategory(name: "Inventions", icon: "lightbulb.fill", color: "#1ABC9C")

    static let all: [TechnologySubcategory] = [videoGames, computersSoftware, internetSocialMedia, techCompanies, inventions]
}

// MARK: - Art Subcategories
struct ArtSubcategory: TriviaSubcategory {
    let name: String
    let icon: String
    let color: String

    static let famousPainters = ArtSubcategory(name: "Famous Painters", icon: "paintbrush.fill", color: "#F7B500")
    static let artHistoryMovements = ArtSubcategory(name: "Art History & Movements", icon: "clock.arrow.circlepath", color: "#FF7F0F")
    static let sculpture = ArtSubcategory(name: "Sculpture", icon: "person.bust.fill", color: "#8E44AD")
    static let architecture = ArtSubcategory(name: "Architecture", icon: "building.fill", color: "#3498DB")
    static let photography = ArtSubcategory(name: "Photography", icon: "camera.fill", color: "#1ABC9C")

    static let all: [ArtSubcategory] = [famousPainters, artHistoryMovements, sculpture, architecture, photography]
}

// MARK: - Geography Subcategories
struct GeographySubcategory: TriviaSubcategory {
    let name: String
    let icon: String
    let color: String

    static let usGeography = GeographySubcategory(name: "U.S. Geography", icon: "mappin", color: "#F7B500")
    static let worldGeography = GeographySubcategory(name: "World Geography", icon: "globe", color: "#FF7F0F")
    static let flags = GeographySubcategory(name: "Flags", icon: "flag.2.crossed.fill", color: "#8E44AD")
    static let landmarksMonuments = GeographySubcategory(name: "Landmarks & Monuments", icon: "building.2.fill", color: "#3498DB")
    static let mapsBorders = GeographySubcategory(name: "Maps & Borders", icon: "map.fill", color: "#1ABC9C")

    static let all: [GeographySubcategory] = [usGeography, worldGeography, flags, landmarksMonuments, mapsBorders]
}
