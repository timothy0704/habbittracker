document.addEventListener("DOMContentLoaded", function () {
    const habitForm = document.getElementById("habit-form");
    const habitList = document.getElementById("habit-list");
    const totalHabits = document.getElementById("total-habits");
    const completedHabits = document.getElementById("completed-habits");

    let habitCount = 0;
    let completedCount = 0;

    habitForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const habitName = document.getElementById("habit-name").value;
        const habitCategory = document.getElementById("habit-category").value;
        const habitFrequency = document.getElementById("habit-frequency").value;

        if (habitName.trim() === "") return;

        const habitItem = document.createElement("div");
        habitItem.classList.add("habit-item");
        habitItem.innerHTML = `
            <p><strong>${habitName}</strong> (${habitCategory} - ${habitFrequency})</p>
            <button class="complete-btn">✔ Complete</button>
        `;

        habitList.appendChild(habitItem);
        habitCount++;
        totalHabits.textContent = habitCount;

        const completeBtn = habitItem.querySelector(".complete-btn");
        completeBtn.addEventListener("click", function () {
            if (!habitItem.classList.contains("completed")) {
                habitItem.classList.add("completed");
                completedCount++;
                completedHabits.textContent = completedCount;
                completeBtn.disabled = true;
            }
        });

        habitForm.reset();
    });
});
