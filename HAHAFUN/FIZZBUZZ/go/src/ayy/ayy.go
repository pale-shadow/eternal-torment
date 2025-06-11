package main

import (
  "fmt"
  "image"
  "image/color"
  "image/png"
  "math"
  "os"
)

func check(e error) {
  if e != nil {
    panic(e)
  }
}

// HLine draws a horizontal line
func HLine(x1, y, x2 int) {
  for ; x1 <= x2; x1++ {
    img.Set(x1, y, col)
  }
}

// VLine draws a veritcal line
func VLine(x, y1, y2 int) {
  for ; y1 <= y2; y1++ {
    img.Set(x, y1, col)
  }
}

// Rect draws a rectangle utilizing HLine() and VLine()
func Rect(x1, y1, x2, y2 int) {
  HLine(x1, y1, x2)
  HLine(x1, y2, x2)
  VLine(x1, y1, y2)
  VLine(x2, y1, y2)
}

type Circle struct {
  X, Y, R float64
}

func (c *Circle) Brightness(x, y float64) uint8 {
  var dx, dy float64 = c.X - x, c.Y - y
  d := math.Sqrt(dx*dx+dy*dy) / c.R
  if d > 1 {
    return 0
  } else {
    return 255
  }
}

var img = image.NewRGBA(image.Rect(0, 0, 100, 100))
var col color.Color

func main() {
  fmt.Printf("Ayy lmao\n")
  col = color.RGBA{255, 0, 0, 255} // Red
  HLine(10, 20, 80)
  col = color.RGBA{0, 255, 0, 255} // Green
  Rect(10, 10, 80, 50)

  f, err := os.Create("draw.png")
  check(err) 

  defer f.Close()
  png.Encode(f, img)

  var w, h int = 280, 240
  var hw, hh float64 = float64(w / 2), float64(h / 2)
  r := 40.0
  θ := 2 * math.Pi / 3
  cr := &Circle{hw - r*math.Sin(0), hh - r*math.Cos(0), 60}
  cg := &Circle{hw - r*math.Sin(θ), hh - r*math.Cos(θ), 60}
  cb := &Circle{hw - r*math.Sin(-θ), hh - r*math.Cos(-θ), 60}

  m := image.NewRGBA(image.Rect(0, 0, w, h))
  for x := 0; x < w; x++ {
    for y := 0; y < h; y++ {
      c := color.RGBA{
        cr.Brightness(float64(x), float64(y)),
	cg.Brightness(float64(x), float64(y)),
	cb.Brightness(float64(x), float64(y)),
        255,
      }
      m.Set(x, y, c)
    }
  }

  q, err := os.OpenFile("rgb.png", os.O_WRONLY|os.O_CREATE, 0600)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer q.Close()
  png.Encode(q, m)
}
