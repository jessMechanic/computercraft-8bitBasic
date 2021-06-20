color = {}
color["0"] = colors.white 
color["1"] = colors.orange
color["2"] = colors.magenta
color["3"] = colors.lightBlue
color["4"] = colors.yellow 
color["5"] = colors.lime
color["6"] = colors.pink
color["7"] = colors.gray
color["8"] = colors.lightGray
color["9"] = colors.cyan
color["a"] = colors.purple
color["d"] = colors.green
color["c"] = colors.brown 
color["e"] = colors.red
color["f"] = colors.black
color["b"] = colors.blue

touch = true

image = {
    ['resolution'] = {
    ["x"] = 1,
    ["y"] = 1
    },
    ['imageData'] = "0"
    
    } 
function display(imageP,x,y)

monitor = peripheral.find("monitor")
    monitor.setTextScale(0.5)
    size = monitor.getSize() 
        if imageP['imageData'] == nil or imageP['resolution'] == nil then
            write("imageData not complete")  
        end
        for Dy = 1, imageP['resolution']['y'] do
            for Dx = 1,imageP['resolution']['x'] do
            count = Dx + ((Dy -1 ) * imageP['resolution']['x'] )
    
            c = string.sub(imageP['imageData'] , count,count)  
              
            
            --  paintutils.drawPixel(Dx + x, Dy + y,colors .red) 
           monitor.setCursorPos(Dx  + x,Dy + y)
           monitor.setBackgroundColor(color[c])
           monitor.write(" ") 
              end
             -- os.sleep(0.4) --to see the scanLines
         end
     return true    
    end
    print("what file do you want to render")
imageName = read()
img = fs.open(imageName,"r")
image['resolution']['x'] = tonumber(img.readLine())
image['resolution']['y'] = tonumber(img.readLine())
image['imageData'] =  img.readLine()
display(image,1,1)
while true do
end

    
