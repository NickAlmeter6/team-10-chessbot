const BACKEND_URL = "http://192.168.52.64:8000";

export async function evaluateMove(fen, move) {
  try {
    console.log(JSON.stringify({ fen, move }))
    const res = await fetch(`${BACKEND_URL}/evaluate`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      
      body: JSON.stringify({ fen, move }),
    });

    const data = await res.json();
    return data;
  } catch (err) {
    console.error("Error evaluating move:", err);
    return null;
  }
}
