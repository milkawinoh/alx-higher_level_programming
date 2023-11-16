#!/usr/bin/node
if (!isNaN(process.argv[2]))
{
    let x = parseInt(process.argv[2]);
    let i;
    for (i = 0; i < x; i++ )
    {
        console.log("x".repeat(x))  

    }
    

}
else
{
    console.log("missing size")
}