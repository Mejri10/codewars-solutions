From <a href='https://en.wikipedia.org/wiki/N-back'>Wikipedia</a> : "The n-back task is a continuous performance task that is commonly used as an assessment in cognitive neuroscience to measure a part of working memory and working memory capacity. [...] The subject is presented with a sequence of stimuli, and the task consists of indicating when the current stimulus matches the one from n steps earlier in the sequence. The load factor n can be adjusted to make the task more or less difficult."

In this kata, your task is to "teach" your computer to do the n-back task. <strong>Specifically, you will be implementing a function that counts the number of "targets" (stimuli that match the one from n steps earlier) in a sequence of digits.</strong> Your function will take two parameters :
<ul>
<li><code>n</code>, a positive integer equal to the number of steps to look back to find a match</li>
<li><code>sequence</code>, a sequence of digits containing 0 or more targets</li>
</ul>

<em>A few hints </em>:
<ul>
<li>The first digit in a sequence can never be a target</li>
<li>Targets can be "chained" together (e.g., for <code>n = 1</code> and <code>sequence = [1, 1, 1]</code>, there are <strong>2</strong> targets)</li>
</ul>