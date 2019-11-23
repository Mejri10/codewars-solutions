def dropzone(fire, dropzones)
  dropzones.sort_by{ |dropzone| Math.hypot(dropzone.last - fire.last, dropzone.first - fire.first) }.first
end