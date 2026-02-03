//
//  StoreFilters.swift
//  Fiz
//
//  Created by Claude on 2/3/26.
//

import Foundation

// MARK: - Topic Filter
enum TopicFilter: String, CaseIterable, Identifiable {
    case all = "All Packs"
    case fantasy = "Fantasy"
    case animation = "Animation"
    case superheroes = "Superheroes"
    case sciFi = "Sci-Fi"
    case comedy = "Comedy"
    case nostalgia = "Nostalgia"
    case sports = "Sports"

    var id: String { rawValue }

    func matches(packId: String) -> Bool {
        switch self {
        case .all: return true
        case .fantasy: return packId.contains("harry_potter") || packId.contains("pokemon")
        case .animation: return packId.contains("disney") || packId.contains("pixar")
        case .superheroes: return packId.contains("dc") || packId.contains("marvel")
        case .sciFi: return packId.contains("star_wars")
        case .comedy: return packId.contains("the_office")
        case .nostalgia: return packId.contains("80s")
        case .sports: return packId.contains("sports")
        }
    }

    // MARK: - Contextual Keywords
    /// Returns searchable contextual keywords for a pack based on its ID
    /// Used to improve search discoverability (e.g., searching "baseball" finds Sports pack)
    static func contextualKeywords(for packId: String) -> [String] {
        switch packId {
        case let id where id.contains("sports"):
            return ["baseball", "basketball", "football", "soccer", "hockey", "tennis", "golf", "athletics", "nfl", "nba", "mlb", "nhl"]
        case let id where id.contains("harry_potter"):
            return ["wizarding", "wizard", "hogwarts", "magic", "witchcraft", "wand", "quidditch", "gryffindor", "slytherin", "muggle"]
        case let id where id.contains("pokemon"):
            return ["pikachu", "creatures", "monsters", "catching", "trainers", "gym", "evolution", "nintendo", "gamefreak"]
        case let id where id.contains("star_wars"):
            return ["jedi", "sith", "lightsaber", "force", "galaxy", "space", "darth vader", "luke skywalker", "yoda", "empire", "rebellion"]
        case let id where id.contains("marvel"):
            return ["avengers", "superhero", "mutants", "xmen", "x-men", "spider-man", "spiderman", "iron man", "captain america", "thor", "hulk", "mcu"]
        case let id where id.contains("dc"):
            return ["batman", "superman", "justice league", "gotham", "metropolis", "wonder woman", "flash", "aquaman", "joker", "dceu"]
        case let id where id.contains("disney"):
            return ["princess", "animated", "fairy tale", "castle", "magic kingdom", "mickey", "minnie", "walt", "classic"]
        case let id where id.contains("pixar"):
            return ["animated", "toy story", "finding nemo", "monsters inc", "cars", "incredibles", "up", "wall-e", "coco"]
        case let id where id.contains("the_office"):
            return ["dunder mifflin", "scranton", "workplace", "sitcom", "michael scott", "dwight", "jim", "pam", "nbc"]
        case let id where id.contains("80s"):
            return ["retro", "eighties", "decade", "vintage", "throwback", "1980s", "classic", "nostalgia"]
        default:
            return []
        }
    }
}

// MARK: - Question Count Filter
enum QuestionCountFilter: String, CaseIterable, Identifiable {
    case all = "All Sizes"
//    case under300 = "Under 300"
    case range300to400 = "300-400"
    case range400to500 = "400-500"
    case over500 = "500+"

    var id: String { rawValue }

    func matches(questionCount: Int) -> Bool {
        switch self {
        case .all: return true
//        case .under300: return questionCount < 300
        case .range300to400: return questionCount >= 300 && questionCount < 400
        case .range400to500: return questionCount >= 400 && questionCount < 500
        case .over500: return questionCount >= 500
        }
    }
}
