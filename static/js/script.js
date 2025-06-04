document.getElementById('form-url').addEventListener('submit', (event)=>{
    event.preventDefault();
    urlInput = event;
    console.log(event.target.url.value);
})