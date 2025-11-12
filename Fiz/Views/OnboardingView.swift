//
//  OnboardingView.swift
//  Fiz
//
//  Created by Claude Code on 8/13/25.
//

import SwiftUI

struct OnboardingView: View {
    @StateObject private var userManager = UserManager.shared
    @State private var enteredName: String = ""
    @State private var showingError = false
    
    var body: some View {
        ZStack {
            LinearGradient(
                colors: [Color.fizBackground, Color.fizBackgroundSecondary],
                startPoint: .topLeading,
                endPoint: .bottomTrailing
            )
            .ignoresSafeArea()
            
            VStack(spacing: 32) {
                Spacer()
                
                // Welcome section with Fiz
                VStack(spacing: 16) {
                    Image("fiz-happy smirk")
                        .resizable()
                        .scaledToFit()
                        .frame(width: 140, height: 140)

                    Text("Welcome to Fiz Trivia!")
                        .font(.largeTitle)
                        .fontWeight(.bold)
                        .foregroundColor(.primary)
                        .multilineTextAlignment(.center)

                    Text("Trivia, just for you")
                        .font(.title2)
                        .foregroundColor(.secondary)
                        .multilineTextAlignment(.center)
                        .padding(.horizontal, 24)
                }
                
                Spacer()
                
                // Name input section
                VStack(spacing: 20) {
                    Text("What should we call you?")
                        .font(.title2)
                        .fontWeight(.semibold)
                        .foregroundColor(.primary)
                    
                    TextField("Enter your name", text: $enteredName)
                        .font(.body)
                        .padding(.horizontal, 16)
                        .padding(.vertical, 12)
                        .background(Color.clear)
                        .overlay(
                            RoundedRectangle(cornerRadius: 12)
                                .stroke(Color.gray.opacity(0.4), lineWidth: 1.5)
                        )
                        .padding(.horizontal, 32)
                        .autocorrectionDisabled()
                        .textInputAutocapitalization(.words)
                    
                    if showingError {
                        Text("Please enter a name to continue")
                            .font(.caption)
                            .foregroundColor(.red)
                            .transition(.opacity)
                    }
                    
                    Button(action: {
                        submitName()
                    }) {
                        Text("Ready to Start!")
                    }
                    .prominentActionButton(color: Color.fizOrange)
                    .padding(.horizontal, 32)
                    .disabled(enteredName.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty)
                    .opacity(enteredName.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty ? 0.6 : 1.0)
                }
                
                Spacer()
                
                // Skip option
                Button(action: {
                    skipOnboarding()
                }) {
                    Text("Skip for now")
                        .font(.subheadline)
                        .foregroundColor(.secondary)
                        .underline()
                }
                .padding(.bottom, 32)
                
                Spacer()
            }
        }
        .onSubmit {
            submitName()
        }
    }
    
    private func submitName() {
        let trimmedName = enteredName.trimmingCharacters(in: .whitespacesAndNewlines)
        
        if trimmedName.isEmpty {
            withAnimation(.easeInOut(duration: 0.3)) {
                showingError = true
            }
            
            // Hide error after 3 seconds
            DispatchQueue.main.asyncAfter(deadline: .now() + 3.0) {
                withAnimation(.easeInOut(duration: 0.3)) {
                    showingError = false
                }
            }
            return
        }
        
        HapticManager.shared.buttonTapEffect()
        userManager.saveUsername(trimmedName)
    }
    
    private func skipOnboarding() {
        HapticManager.shared.buttonTapEffect()
        userManager.saveUsername("Player")
    }
}

#Preview("Light Mode") {
    OnboardingView()
        .preferredColorScheme(.light)
}

#Preview("Dark Mode") {
    OnboardingView()
        .preferredColorScheme(.dark)
}
