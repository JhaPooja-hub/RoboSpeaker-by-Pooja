// Fetch events from backend
fetch("http://127.0.0.1:5000/events")
.then(res => res.json())
.then(events => {
    const container = document.getElementById("events");
    events.forEach(event => {
        const card = document.createElement("div");
        card.className = "event-card";
        card.innerHTML = `
            <h3>${event.name}</h3>
            <p>📅 ${event.date}</p>
            <p>📍 ${event.place}</p>
        `;
        container.appendChild(card);
    });
})
.catch(err => {
    console.error("Error fetching events:", err);
});
