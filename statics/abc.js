
console.log("called")

function addinInputField(component)

{
    let firstValue = document.getElementById("userSelection").value;
  if(component.id=="1")
  {
    console.log("First is Called")
    document.getElementById("userSelection").value=firstValue+'123'
    
  }
  else if(component.id=="2")
  {
    console.log("2nd is Called")
  }
  else if(component.id=="3")
  {
    console.log("Thir is Called")
  }
}