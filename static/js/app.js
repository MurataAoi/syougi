//ドラッグ＆ドロップの処理
class DragPiece {
	dragElement = null;

	constructor(){
	}

	init(table){
		const tdList = table.querySelectorAll("td");
		for (const td of tdList){
			td.addEventListener("dragstart", (event) => this.dragElement = event.target );
			td.addEventListener("dragover", (event) => event.preventDefault() ); //デフォルトの動作を禁止
			td.addEventListener("drop", (event) => {
				//デフォルトの動作を禁止。
				event.preventDefault();
				//ドラッグ中の要素をドロップした td に移動する。
				if (event.target.tagName == "TD"){
					this.dragElement.parentNode.removeChild( this.dragElement);
					event.target.appendChild( this.dragElement);
				}
			});
		}
	}
}

window.onload = function(){
	const table = document.querySelector(".board");
	const drag = new DragPiece();
	drag.init(table);
}