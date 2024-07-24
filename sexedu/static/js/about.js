document.addEventListener("DOMContentLoaded", () => {
  const section = document.querySelector(".ourteam");
  const showBtn = document.querySelector(".show-form"); 
  const closeBtn = document.querySelector(".close-btn"); 
  showBtn.addEventListener("click", () => {
      section.classList.add("active");
  });
  
   closeBtn.addEventListener("click", () => {
        section.classList.remove("active");
    });
});

