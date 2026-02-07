//
//  WhatsNewModels.swift
//  Fiz
//
//  Extracted from TriviaModels.swift during code review refactor
//

import Foundation

struct WhatsNewUpdate: Identifiable {
    let id = UUID()
    let version: String
    let title: String
    let features: [WhatsNewFeature]
}

struct WhatsNewFeature: Identifiable {
    let id = UUID()
    let icon: String
    let title: String
    let description: String
}
