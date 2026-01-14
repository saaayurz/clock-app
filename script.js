let use24Hour = true;

function updateTime() {
    const now = new Date();

    let hours = now.getHours();
    let minutes = now.getMinutes();
    let seconds = now.getSeconds();
    let suffix = "";

    if (!use24Hour) {
        suffix = hours >= 12 ? " PM" : " AM";
        hours = hours % 12 || 12;
    }

    minutes = String(minutes).padStart(2, "0");
    seconds = String(seconds).padStart(2, "0");

    document.getElementById("time").innerText =
        `${hours}:${minutes}:${seconds}${suffix}`;

    document.getElementById("date").innerText =
        now.toDateString();
}

setInterval(updateTime, 1000);
updateTime();

document.getElementById("formatBtn").onclick = function () {
    use24Hour = !use24Hour;
    this.innerText = use24Hour ? "24h" : "12h";
};
function setTheme(themeName) {
    document.body.className = themeName;
}
async function updateWeather() {
    try {
        const response = await fetch(
            "https://api.open-meteo.com/v1/forecast?latitude=21.15&longitude=79.09&current_weather=true"
        );
        const data = await response.json();
        const temp = data.current_weather.temperature;

        document.getElementById("weather").innerText =
            `Nagpur: ${temp}°C`;
    } catch (error) {
        document.getElementById("weather").innerText =
            "Weather unavailable";
    }
}

updateWeather();
setInterval(updateWeather, 600000);
