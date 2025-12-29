import SwiftUI

struct UsernameSettingsView: View {
    @StateObject private var userManager = UserManager.shared
    @State private var editedUsername: String = ""
    @State private var isEditingUsername = false

    var body: some View {
        Form {
            Section(footer: Text("Your username is used to personalize messages throughout the app.")) {
                if isEditingUsername {
                    HStack {
                        TextField("Enter username", text: $editedUsername)
                            .textFieldStyle(RoundedBorderTextFieldStyle())
                            .autocorrectionDisabled()
                            .textInputAutocapitalization(.words)
                            .onSubmit {
                                saveUsername()
                            }

                        Button("Save") {
                            saveUsername()
                        }
                        .font(.caption)
                        .foregroundColor(.blue)

                        Button("Cancel") {
                            cancelEditing()
                        }
                        .font(.caption)
                        .foregroundColor(.secondary)
                    }
                } else {
                    Button(action: { startEditing() }) {
                        HStack {
                            Text(userManager.displayName)
                                .foregroundColor(.primary)
                            Spacer()
                            Text("Edit")
                                .foregroundColor(.blue)
                        }
                    }
                }
            }
        }
        .navigationTitle("Username")
        .navigationBarTitleDisplayMode(.large)
    }

    private func startEditing() {
        editedUsername = userManager.username
        isEditingUsername = true
    }

    private func saveUsername() {
        let trimmedName = editedUsername.trimmingCharacters(in: .whitespacesAndNewlines)
        if !trimmedName.isEmpty {
            userManager.updateUsername(trimmedName)
            HapticManager.shared.buttonTapEffect()
        }
        isEditingUsername = false
        editedUsername = ""
    }

    private func cancelEditing() {
        isEditingUsername = false
        editedUsername = ""
    }
}

#Preview {
    NavigationStack {
        UsernameSettingsView()
    }
}
