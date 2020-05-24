# not used

require 'pp'

def Pcc(a, b, n)
	vertex = (1..n).to_a
	edge = []
	for x in 1..vertex.length
		for y in x+1..vertex.length
			edge.append(x.to_s + "-" + y.to_s)
		end
	end
	puts edge

	for trial in 0..2**edge.length-1
		coloring = {}
		binaryTrial = trial.to_s(2)
		trialcode = "0" * (edge.length-binaryTrial.length) + binaryTrial
		puts "TRIAL " + trial.to_s + " WITH TRIAL CODE " + trialcode
		for l in 0..trialcode.length-1
			coloring[edge[l]] = trialcode[l]
		end
		pp coloring
		puts ""
	end

	
end

Pcc(3, 4, 5)