def work_needed(project_minutes, freelances)
  freelance_minutes = freelances.reduce(0){ |sum, (h, m)| sum + h*60 + m }
  if freelance_minutes >= project_minutes
    "Easy Money!"
  else
    diff = project_minutes - freelance_minutes
    hours = diff / 60
    minutes = diff % 60
    "I need to work #{hours} hour(s) and #{minutes} minute(s)"
  end
end