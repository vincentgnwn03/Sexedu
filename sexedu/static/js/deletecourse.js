// Function to delete accordion content
function deleteAccordionContent(element) {
    // Remove from localStorage
    const accordionContents = JSON.parse(localStorage.getItem('accordionContents')) || [];
    const index = Array.from(accordion.children).indexOf(element);
    accordionContents.splice(index, 1);
    localStorage.setItem('accordionContents', JSON.stringify(accordionContents));

    // Remove from DOM
    element.remove();
}

// Event delegation for delete button
accordion.addEventListener('click', function (e) {
    if (e.target.classList.contains('btn-delete')) {
        const accordionContent = e.target.closest('.accordion-content');
        deleteAccordionContent(accordionContent);
    }
});
