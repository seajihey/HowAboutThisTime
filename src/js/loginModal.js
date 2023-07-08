const openButton = document.getElementById("open");
const modal = document.querySelector(".modal");
const overlay = modal.querySelector(".modalOverlay");
const closeBtn = modal.querySelector(".closeBtn");
const openModal = () => {
    modal.classList.remove("hidden");
}
const closeModal = () => {
    modal.classList.add("hidden");
}
overlay.addEventListener("click",closeModal);
closeBtn.addEventListener("click",closeModal);
openButton.addEventListener("click",openModal);