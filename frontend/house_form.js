const form = document.getElementById("house-form");
const result = document.getElementById("result");
const submitButton = form.querySelector('button[type="submit"]');

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const formData = new FormData(form);
    const params = new URLSearchParams({
        area: formData.get("area"),
        bedrooms: formData.get("bedrooms"),
        location: formData.get("location")
    });

    result.textContent = "Đang dự đoán...";
    submitButton.disabled = true;

    try {
        const response = await fetch(`/predict?${params.toString()}`);

        if (!response.ok) {
            throw new Error("API trả về lỗi " + response.status);
        }

        const data = await response.json();
        result.textContent = "Giá nhà dự đoán: " + data.predicted_price;
    } catch (error) {
        result.textContent = "Không thể kết nối tới API. Hãy kiểm tra backend đã chạy chưa.";
        console.error(error);
    } finally {
        submitButton.disabled = false;
    }
});
