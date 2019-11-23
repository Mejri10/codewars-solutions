def printer_error(s)
	"#{s.scan(/[^a-m]/).length}/#{s.length}"
end