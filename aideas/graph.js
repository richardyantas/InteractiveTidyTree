
var id = 0
function CNode()
{
    this.id = id++;
    this.name = "";
    this.children = [];
    this.parent = null;
}

function addEdge(v,w)
{
    v.children.push(w);
    w.parent = v
}

a = new CNode();
a.name = "rich";

b = new CNode()
b.name = "sun";

a.children.push(b);
b.parent = a;

console.log(a.children[0].parent)