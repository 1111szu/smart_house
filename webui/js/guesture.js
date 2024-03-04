const checkboxes = document.querySelectorAll(".switch-input");

checkboxes.forEach((checkbox) => {
    checkbox.addEventListener("change", function(event) {
        if (checkbox.checked) {
            // 开灯信号
            
        } else {
            // 关灯信号
            
        }
    });
});

onmessage