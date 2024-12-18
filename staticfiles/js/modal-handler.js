document.addEventListener("DOMContentLoaded", function () {
    const messages = JSON.parse(
        document.getElementById("django-messages").textContent
    );
    if (messages.length > 0) {
        const messageText = messages.join("\n");
        const modalBody = document.getElementById("modal-body");
        if (modalBody) {
            modalBody.textContent = messageText;
            const myModal = new bootstrap.Modal(document.getElementById("messageModal"));
            myModal.show();
        }
    }
});
