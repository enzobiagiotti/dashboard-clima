async function buscarClima() {
  const cidade = document.getElementById("cidade").value;
  const estado = document.getElementById("estado").value;
  const pais = document.getElementById("pais").value;
  const resultado = document.getElementById("resultado");

  resultado.innerHTML = "Buscando...";

  try {
    const res = await fetch(`http://localhost:5000/clima?cidade=${cidade}&estado=${estado}&pais=${pais}`);
    const dados = await res.json();

    if (!res.ok) {
      resultado.innerHTML = `<span class="erro">Erro: ${dados.erro}</span>`;
      return;
    }

    resultado.innerHTML =
      `<strong>${Math.round(dados.temperatura)}°C</strong> — ${dados.descricao}\n` +
      `Mínima: ${Math.round(dados.minima)}°C   Máxima: ${Math.round(dados.maxima)}°C\n` +
      `Umidade: ${dados.umidade}%`;
  } catch (erro) {
    resultado.innerHTML = `<span class="erro">Erro ao conectar com o backend. Ele está rodando?</span>`;
  }
}