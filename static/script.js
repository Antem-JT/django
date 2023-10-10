// script.js

document.addEventListener("DOMContentLoaded", () => {
    const notesList = document.getElementById("notes-list");
    const noteText = document.getElementById("note-text");
    const addNoteButton = document.getElementById("add-note");

    addNoteButton.addEventListener("click", () => {
        const noteContent = noteText.value.trim();
        if (noteContent !== "") {
            const li = document.createElement("li");
            li.textContent = noteContent;
            notesList.appendChild(li);
            noteText.value = "";
        }
    });
});
