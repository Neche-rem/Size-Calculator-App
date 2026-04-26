async function calculate() {
    const image_size = document.getElementById("image_size").value;
    const magnification = document.getElementById("magnification").value;

    const response = await fetch("/calculate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            image_size,
            magnification
        })
    });

    const data = await response.json();

    if (data.error) {
        document.getElementById("result").innerText = data.error;
    } else {
        document.getElementById("result").innerText =
            "Actual Size: " + data.actual_size + " mm";
    }
}
