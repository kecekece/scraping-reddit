document.getElementById('form-url').addEventListener('submit', (event)=>{
    event.preventDefault();
    urlInput = event.target.url.value;
    console.log(urlInput);

    axios.post('/', {
        url : urlInput,
    }).then((result) => {
        comments = result.data;
        // console.log(comments);
        document.getElementById('total-comment').innerText = comments.length;

        const tableBody = document.getElementById('data-scraping');
        comments.forEach((comment, index) => {
            const row = document.createElement('tr');

            const tdNo = document.createElement('td');
            tdNo.textContent = index + 1;

            const tdAuthor = document.createElement('td');
            tdAuthor.textContent = comment.author;

            const tdComment = document.createElement('td');
            tdComment.textContent = comment.body;

            const tdTime = document.createElement('td');
            tdTime.textContent = comment.created_at;

            row.appendChild(tdNo)
            row.appendChild(tdAuthor)
            row.appendChild(tdComment)
            row.appendChild(tdTime)

            tableBody.appendChild(row)
        });
        
    }).catch((err) => {
        console.log(err);
        
    });
})