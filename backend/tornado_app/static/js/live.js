function render(d) {
  const tbody = document.getElementById("rows");
  tbody.replaceChildren();
  d.rows.forEach((r, i) => {
    const tr = document.createElement("tr");
    [i + 1, r.username, r.points, r.best, r.games].forEach(v => {
      const td = document.createElement("td");
      td.textContent = v;
      tr.appendChild(td);
    });
    tbody.appendChild(tr);
  });
  document.getElementById("status").textContent = "Mivantana (live) - " + d.online + " mpijery";
}

function connect() {
  const proto = location.protocol === "https:" ? "wss" : "ws";
  const ws = new WebSocket(proto + "://" + location.host + "/ws");
  ws.onmessage = e => render(JSON.parse(e.data));
  ws.onclose = () => {
    document.getElementById("status").textContent = "Mifandray indray...";
    setTimeout(connect, 2000);
  };
}

connect();
