const apiBase = "http://localhost:5000";

function loadEntries() {
    fetch(`${apiBase}/entries`)
        .then(res => res.json())
        .then(data => {
            const list = document.getElementById('entries');
            list.innerHTML = '';
            data.forEach(entry => {
                const li = document.createElement('li');
                li.textContent = entry.content;
                list.appendChild(li);
            });
        });
}

function submitEntry() {
    const content = document.getElementById('entry').value;
    fetch(`${apiBase}/entries`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ content })
    }).then(() => {
        document.getElementById('entry').value = '';
        loadEntries();
    });
}

loadEntries();
