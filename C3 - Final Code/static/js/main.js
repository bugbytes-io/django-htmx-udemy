let clearForm = () => {
    let form = document.getElementById('book-form');
    document.getElementById('form-errors').replaceChildren();
    form.querySelectorAll("input:not([name='csrfmiddlewaretoken'])").forEach(
        input => input.value = ''
    );

    form.querySelectorAll('select').forEach(select => select.selectedIndex = 0);

    document.querySelectorAll('.form-field-errors').forEach(errorField => {
        errorField.replaceChildren();
    });
    
    removeEmptyBooksMessage()
}

let removeEmptyBooksMessage = () => {
    let emptyRow = document.querySelector('.empty-message')
    if (emptyRow) {
        emptyRow.remove()
    }
}

let fadeOutAndRemove = (tr) => {
    tr.style.transition = 'opacity .5s ease'
    tr.style.opacity = 0
    setTimeout(() => tr.remove(), 500)
}