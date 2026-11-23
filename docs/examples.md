# Example comparisons

These examples are **not hand-picked**. Selection rule, fixed before reading them: the first test-split task in each of six categories (naming, headlines, marketing, short story, rewrite, brainstorm), sample 0, from both generator models, run `v3`. Every arm's output is shown in full as judged. The judges' verdicts on each pair are listed so the reader can disagree with them. A separate section shows the lowest-scoring task, chosen by the same automatic ranking the report uses.

Arms: **baseline** ("You are a helpful assistant."), **one-liner** ("...Be original: avoid cliches and look past the first, most obvious idea."), **Bohemian** (the skill). Same model, temperature, token budget and user message in each.

## naming-2

> Suggest 5 names for a small coffee roastery. One per line, nothing else.

### deepseek/deepseek-v4.1-flash

**Baseline**

```text
Ember & Oak Coffee
Harbor Roast Works
Wildroot Coffee Co.
Copper Kettle Roasters
Northlight Coffee Roasters
```

**One-liner**

```text
Ember & Origin
The Slow Burn
Grumpy Badger Roasters
Second Crack Society
Moth & Kettle
```

**Bohemian**

```text
Ash & Ember
Third Crack
The Loud Cup
Tuesday Roast
Little Bolt Coffee
```

*Judges:* vs baseline: gemini-2.5-flash-lite: prefer=Bohemian; gpt-4o-mini: prefer=Bohemian. vs one-liner: gemini-2.5-flash-lite: prefer=oneliner; gpt-4o-mini: prefer=oneliner.

### anthropic/claude-haiku-5.5

**Baseline**

```text
Ember & Bean Roasters
Hollow Oak Coffee Co.
Driftwood Roastery
Cinder Lane Coffee
Parallel Roast Works
```

**One-liner**

```text
Ember & Orbit
Low Tide Roasters
Parallel Bean Co.
Hollow Kettle
Second Crack Ledger
```

**Bohemian**

```text
Ember & Ledger
Tidewater Roasters
Coldwater Grind
Gravel & Gold
Second Hand Roasting
```

*Judges:* vs baseline: gemini-2.5-flash-lite: prefer=Bohemian; gpt-4o-mini: prefer=Bohemian. vs one-liner: gemini-2.5-flash-lite: prefer=oneliner; gpt-4o-mini: prefer=oneliner.

## headlines-2

> Write 5 headlines for a news story about a town that banned cars from its center. One per line, nothing else.

### deepseek/deepseek-v4.1-flash

**Baseline**

```text
Town Bans Cars From Center in Bid to Reclaim Streets for People
Car-Free Comeback: Town Center Shuts Out Vehicles
No Cars Allowed: Town’s Bold Move to Transform Its Center
Town Pulls the Plug on Traffic in Downtown Car Ban
From Parking Lots to People: Town Center Goes Car-Free
```

**One-liner**

```text
No Engines, No Problem: This Town Bet Its Downtown on Foot Traffic — and Won
The Quietest Revolution: How One Town Traded Parking Spots for Park Benches
They Erased Every Parking Meter in the Center. Local Shops Are Thriving.
What Happens When a Town Says 'Walk, Don't Drive'? Nothing Anyone Expected
Zero Cars, Full Cafes: The Unlikely Blueprint From a Town That Ripped Out Its Roads
```

**Bohemian**

```text
Town Council Votes to Close Center to Cars, Starting Monday
Delivery Vans Get Two Hours. Everyone Else Walks.
The Main Street Experiment: Shops Watch, Traffic Counters Click
She Drove the Same Route for 22 Years. Next Week She Takes the Bus.
What the Town Center Sounds Like Without Engines
```

*Judges:* vs baseline: gemini-2.5-flash-lite: prefer=Bohemian; gpt-4o-mini: prefer=Bohemian. vs one-liner: gemini-2.5-flash-lite: prefer=oneliner; gpt-4o-mini: prefer=oneliner.

### anthropic/claude-haiku-5.5

**Baseline**

```text
Town Bans Cars From Center, Residents Cheer the Quiet Streets
Downtown Goes Car-Free as Pedestrian Zone Opens to Public
Cars Out, Cafés In: Inside the Town's Bold Traffic Experiment
Merchants Split Over New Car-Free Center Rules
After Car Ban, Town Center Sees Surge in Foot Traffic
```

**One-liner**

```text
Main Street Goes Quiet as Town Trades Engines for Footsteps
Council Votes to Hand the Center Back to Pedestrians and Pigeons
Parking Spaces Become Picnic Tables in Bold Downtown Experiment
Shopkeepers Split on Car-Free Plan as Foot Traffic Doubles
Residents Learn to Hear Their Own Conversations Again After Ban
```

**Bohemian**

```text
Town Center Goes Car-Free as Main Street Reopens to Pedestrians
Residents Trade Parking Spaces for Benches After Center Closes to Traffic
Shop Owners Split Over Downtown Car Ban: Some Report Record Foot Traffic
Ban on Cars in Old Town Center Passes Council Vote by Narrow Margin
Drivers Circle, Kids Reclaim the Square: Inside the Town's Car-Free Experiment
```

*Judges:* vs baseline: gemini-2.5-flash-lite: prefer=Bohemian; gpt-4o-mini: prefer=Bohemian. vs one-liner: gemini-2.5-flash-lite: prefer=oneliner; gpt-4o-mini: prefer=oneliner.

## marketing-2

> Write a 60-word product description for a stainless steel water bottle.

### deepseek/deepseek-v4.1-flash

**Baseline**

```text
Stay hydrated in style with this premium stainless steel water bottle. Double-wall vacuum insulation keeps drinks cold for 24 hours or hot for 12. Durable, leak-proof, and BPA-free, it resists rust and flavor transfer. The sleek, sweat-proof design fits most cup holders and backpacks. Eco-friendly and built to last—your perfect companion for gym, office, or adventure.
```

**One-liner**

```text
Forged from single-wall 18/8 steel, this bottle refuses to sweat, refuses to dent, refuses to flavor your water with yesterday's coffee. Ice stays ice through a heatwave; tea stays hot through a snowstorm. The cap seals with a quarter-turn—no leaks, no drama. It ages like a good knife: scratched, trusted, yours.
```

**Bohemian**

```text
This bottle has no opinions. It holds water, or coffee, or last night's tea. Stainless steel, so it dents instead of shattering, and clanks against a car door the way things do when they've been dropped a few times. No app, no reminder, no personality. Fill it. Cap it. Forget it on a desk and find it Tuesday. It'll still be cold.
```

*Judges:* vs baseline: gemini-2.5-flash-lite: prefer=Bohemian; gpt-4o-mini: prefer=Bohemian. vs one-liner: gemini-2.5-flash-lite: prefer=oneliner; gpt-4o-mini: prefer=oneliner.

### anthropic/claude-haiku-5.5

**Baseline**

```text
Stay hydrated in style with this durable stainless steel water bottle. Double-wall vacuum insulation keeps drinks cold for 24 hours or hot for 12. Leak-proof lid, BPA-free construction, and a sweat-resistant finish make it ready for the gym, office, or trail.
```

**One-liner**

```text
Most bottles sweat onto your desk; this one keeps its grip dry. Double-walled steel holds cold water chilled through a full workday, and a matte finish hides fingerprints and scratches. Drop it on pavement and it will simply shrug. Built for the commute, the lecture hall, and the long afternoon that no bottle was supposed to outlast.
```

**Bohemian**

```text
Cold stays cold for a full day. Hot stays hot through the morning commute. The double-wall stainless steel body sweats nothing onto your desk, and the leak-proof lid twists shut before it goes in your bag. Built to last through dropped gym bags, long hikes and daily wear. Fits most cup holders, and it's easy to clean, dishwasher-safe lid included.
```

*Judges:* vs baseline: gemini-2.5-flash-lite: prefer=Bohemian; gpt-4o-mini: prefer=Bohemian. vs one-liner: gemini-2.5-flash-lite: prefer=oneliner; gpt-4o-mini: prefer=oneliner.

## short_story-2

> Write a short story, 400-600 words, about a wedding where something goes wrong.

### deepseek/deepseek-v4.1-flash

**Baseline**

```text
Maya had planned the wedding for eleven months. She had a spreadsheet for the spreadsheet. She had a color-coded seating chart, a rain contingency inside a rain contingency, and a binder labeled WEDDING — MASTER that she kept under her bed like a loaded weapon.

What she did not have was the right officiant.

The mix-up was nobody's fault, which somehow made it worse. The couple had booked a jolly, bearded celebrant named Thomas Bell. He came highly recommended. He had a warm voice, a calm manner, and a habit of saying "love is a verb" in a way that made everyone nod.

But there was another Thomas Bell in the city directory. Thomas Bell the retired podiatrist. Thomas Bell who, at seventy-three, had never officiated a wedding in his life and had, in fact, been mildly offended when asked.

"Me?" said the wrong Thomas Bell, standing at the altar in a borrowed robe two sizes too large. "I thought you were hiring me to park cars."

Maya looked at him. Maya looked at her groom, Sam, who was trying very hard not to laugh. Maya looked at the two hundred guests, the string quartet, the four thousand dollars of peonies.

"Say something," she hissed.

The retired podiatrist cleared his throat. He was nervous. His hands shook. But he looked out at the crowd, and then at Maya and Sam, and something in his face softened.

"I don't know much about weddings," he said. "But I know feet. Forty years of feet. And I'll tell you what I learned. Everybody's a little crooked. Everybody's got a bone that didn't set right. And you don't love the foot because it's perfect. You love it because it's yours."

There was a pause. Then someone laughed — not cruelly, just surprised. Then someone else. Then the whole tent was laughing, and Maya was laughing too, and then, impossibly, she was crying, and Sam was holding her hand so hard it hurt.

"Now," said the wrong Thomas Bell, "I believe there's a part where you say some things."

They said the things. They said them badly, and they said them anyway. The wrong Thomas Bell pronounced them husband and wife with the solemnity of a man who had once removed a bunion from a bride's grandmother. The string quartet, desperately behind schedule, launched into the recessional four bars late.

And Maya, who had planned everything, discovered that she had not planned for this: the specific, crooked, unrepeatable joy of a wedding where nothing went right and everything went fine.

They kept the binder. They never opened it again.
```

**One-liner**

```text
Dale had married people before, but never with a dummy on his arm. That was the problem with hiring a retired ventriloquist as your officiant: he came as a package deal.

The package was named Mr. Pibbs, a lacquered gentleman in a tiny tuxedo, and he sat on the altar table beside the unity candles like a groomsman who’d been embalmed mid-toast.

Mira had known. She’d booked Dale because he was cheap and because he’d made her laugh at her sister’s funeral, which was the only time she’d laughed that year. She’d told him: no dummy. Dale had nodded, said “Of course,” and then, apparently, developed a selective memory.

So when the processional ended and Dale stepped up to the microphone, Mr. Pibbs already perched beside him, jaw slack, eyes fixed on the back fence, the eighty guests went quiet in that specific way that means *we are all watching the same thing and none of us will say it.*

“Dearly beloved,” Dale said. His lips moved. Mr. Pibbs’s didn’t. “We are gathered—”

The dummy’s head swiveled.

“—to witness something,” Mr. Pibbs finished, “that I personally find premature.”

A ripple. Mira’s mother made a sound like a teakettle. The groom, Jonah, looked at Mira. Mira looked at the sky.

“Dale,” she said, sweetly. “The dummy.”

“He’s part of the ceremony,” Dale said, in his own voice.

“He is not.”

“He’s the best man.”

“My brother is the best man.”

“Your brother is drunk.”

This was true. Her brother was currently trying to untangle a string of fairy lights from a lilac bush, muttering about how the whole thing was rigged.

Jonah stepped forward. He was a quiet man, a carpenter, someone who measured twice. He took the microphone from Dale’s hand. He did not look at Mr. Pibbs. He looked at Mira.

“I wrote vows,” he said. “Then I rewrote them. Then I threw them out because they sounded like a Hallmark card. So here’s the real one.”

He put his hand in his pocket and pulled out a small wooden bird, unpainted, rough at the wing.

“I made this the first week we met. I was going to throw it away because the beak was wrong. You said, *It’s not wrong, it’s just looking somewhere else.* I’ve been looking somewhere else my whole life. You’re the first person who didn’t ask me to turn my head.”

The guests were silent. Mr. Pibbs’s jaw had somehow closed.

Mira took the bird. She held it up. The beak pointed at the fence, at the neighbor’s dog watching through the slats.

“It’s still looking somewhere else,” she said.

“Yeah,” Jonah said. “But now I know where.”

Dale, forgotten, picked up Mr. Pibbs and tucked him under his arm like a football. The dummy’s eyes caught the string lights, and for a second they seemed to glitter. Then Dale walked to the back of the yard and sat down in a folding chair, and the dummy sat beside him, and neither of them said another word.

The ceremony went on. The vows were short. The kiss was longer.

Afterward, someone asked Mira if she was angry about the dummy. She looked over at Dale, who was feeding Mr. Pibbs a piece of cake with a tiny fork.

“No,” she said. “It’s not wrong. It’s just looking somewhere else.”
```

**Bohemian**

```text
Something Goes Wrong at Marta and Dev's Wedding

The thing that went wrong was the chairs.

Not the weather — the weather was fine, overcast and mild, the kind of day that makes people say the light is flattering and mean it. Not the food, which arrived on time and was eaten. The chairs.

Ninety-six chairs had been delivered on Friday to the field behind the Reilly place, and Marta's cousin Petey, who is nineteen and owns a truck, had been given the job of arranging them because he was the only one with a truck and the only one with nothing else to do. He arranged them in rows facing the old maple. He counted them twice. He felt good about the chairs.

What nobody knew, including Petey, including the rental company, was that the field had been an orchard once, and the row of chairs at the back — the last three rows, the ones farthest from the tree — sat on the old irrigation tile. Clay pipe, laid in 1948, mostly collapsed, holding up about a foot of topsoil and ninety-six rented folding chairs.

The ceremony was at four. At 4:11, during the part where Dev's brother was doing the reading and doing it badly, the ground made a sound like a distant cough.

Marta's grandmother Eileen, eighty-six, was in the fourth row from the back. She felt her chair lean. She had been at enough of these to know that the correct thing was to stand up and look annoyed, so she did that first, and the row behind her went down anyway, twelve chairs folding into the earth like a mouth closing, and then Eileen sat down hard on the grass, which she later described as "not the worst thing that has ever happened to me, but close."

Nobody was hurt. That is the first thing people ask and the answer is nobody was hurt. But the back three rows were gone, and about forty guests were standing in a hole, and the reading had stopped, and Dev's brother was still holding the paper, and the whole field was very quiet.

Then Marta started laughing. Not the nervous kind. The kind where you have to sit down, which she did, in the front row, in her dress, on the ground, and then Dev was laughing, and then the people in the hole were laughing, and Eileen was laughing and also being helped up by two men who had been in the back rows and were now, technically, standing in a ditch in their good shoes.

Somebody's kid found the pipe. He held up a piece of it, wet and orange, and said it looked like a bone, and everyone agreed it did.

They finished the ceremony standing. All ninety-six chairs were abandoned where they were, and the guests stood in a loose half-circle around the maple, in the grass, and Marta and Dev said the rest of it there, with the ground open behind them like a page that had been torn.

Afterward, people kept going back to look at the hole. Somebody put a folding chair down in it, upright, and took a picture. Eileen, who has outlived two husbands and a brother and is not sentimental about furniture, said it was the first wedding she had ever been to where you could see what was underneath.
```

*Judges:* vs baseline: gemini-2.5-flash-lite: prefer=Bohemian; gpt-4o-mini: prefer=baseline. vs one-liner: gemini-2.5-flash-lite: prefer=oneliner; gpt-4o-mini: prefer=oneliner.

### anthropic/claude-haiku-5.5

**Baseline**

```text
The cards were the problem. Margaret had typed them herself three weeks earlier, twelve neat pages in a font she'd chosen for its warmth, and she had printed them at the library because the office printer was temperamental. Somewhere between the library and the garden at the Whitfield estate, the stack had been swapped for another, and nobody noticed until Father Dominic lifted the first page under the white-and-gold arch and began, in a clear voice, to read about a man named Gerald Pruitt.

"Gerald was a man who never once returned a library book on time," he said, and a ripple of uncertain laughter moved through the rows of folding chairs. "He kept every receipt he'd ever been given. He believed that a good sandwich was a moral achievement."

Margaret, seated in the front row beside her husband, felt her face go hot. Her daughter Claire, in the ivory gown Margaret had altered twice, turned around with an expression of pure bewilderment. Beside the bride stood Daniel, the groom, who looked toward the officiant with the polite patience of a man who assumed this was some sort of ceremony he hadn't been briefed on.

"Who is Gerald?" Claire whispered, loud enough for the second row.

"I have no idea," Margaret whispered back.

Father Dominic squinted at the page. He flipped it over, then back again. He looked up at the guests, then down at the notes, and something in his shoulders gave way. "I believe," he said slowly, "I have been given the wrong cards. Forgive me. Gerald Pruitt is, apparently, someone's grandfather, and I am very sorry he is being eulogized at a wedding."

The laughter came properly this time, warm and relieved. Somebody in the back called out, "He sounds like a good man!" and another voice agreed.

Margaret stood. She didn't plan to, but she found herself on her feet and walking toward the arch, her heels sinking slightly into the lawn. She had prepared a speech for the reception, but nothing for this. She took the stack of pages from Father Dominic's hands, flipped through them, and found, at last, her own handwriting on the seventh page, a line she had underlined twice: *Claire, you have always met the world with your whole heart. Don't ever apologize for that.*

She looked at her daughter. Claire's eyes were already wet.

"I think," Margaret said, her voice shakier than she wanted, "that Gerald Pruitt would approve of this wedding. Someone who keeps every receipt is someone who believes things are worth remembering. And we are here today to remember that these two people have chosen each other, which is the most worth-remembering thing I know."

She sat down. Father Dominic cleared his throat, found his own real pages, which had been in his jacket pocket the whole time, and began again from the beginning.

Later, at the reception, Daniel found Margaret by the dessert table and said, "I didn't know Gerald Pruitt," and she said, "Neither did I," and they both laughed until the caterer asked whether they needed more champagne.

When people asked afterward what had gone wrong at Claire's wedding, Margaret always gave the same answer. Nothing, really. The wrong man was buried that afternoon, in a sense, but the right words found their way to the right people in the end. That was the part she remembered.
```

**One-liner**

```text
The Bride's Grandmother Goes to the Reception

The caterer's walk-in freezer died at 4:12 in the afternoon, forty minutes before the guests were due in the garden. Marisol Teague discovered this because she was the one who opened the door to check on the sorbet, and the cold that rolled out was the wrong kind, warm and damp and smelling faintly of rotting strawberries.

She had planned this wedding for eleven months. She knew where every chair was numbered, which cousin could not be seated near which uncle, and that the bride, Ines, would cry at the vows whether or not anyone expected it. What she had not planned for was the cooler.

The cooler belonged to Ines's aunt Pilar, who had driven it over from Tucson in the back of a borrowed Subaru. Inside, packed in ice and wrapped in a dish towel, was the grandmother. Everyone knew this, in the vague way families know things: Abuela Rosa's ashes would be "present" at the reception, in a small urn beside the cake, so that she could see her granddaughter married. Marisol had approved the urn placement herself. What she had not approved was the cooler, which Pilar had insisted on because the urn was "too precious to sit in a hot car."

Now the cooler sat on a folding table in the service corridor, its lid sweating, the ice reduced to slush.

Marisol lifted the lid and stared. Then she laughed, once, a sound that startled the busboy. The ice was gone. The towel was soaked. The urn, a heavy bronze thing shaped like a shell, was sitting in a pool of meltwater, perfectly fine, perfectly dry where the lid had kept it, and inscribed in small letters: ROSA ELENA DELGADO, WHO WOULD NOT HAVE LET US IN THE KITCHEN BUT WOULD HAVE FED US ALL.

"We can't serve the cake with her in a puddle," the busboy said.

"No," Marisol agreed, and then she did something she had never done in eleven years of events. She took off her headset, pulled a clean linen napkin from a stack, and dried the urn herself, slowly, while the string quartet tuned in the next room and the florist's van idled outside.

When Ines came looking for her, veil pinned up and mascara already threatening, Marisol was sitting on an overturned milk crate in her good heels.

"The freezer's out," she said. "Your grandmother got a little wet. She's fine."

Ines sat down beside her on the crate. For a moment neither spoke. Then Ines said, "She'd have hated this. Someone fussing over her."

"Probably."

"She'd have said the caterers were thieves."

"They are a little," Marisol said, and Ines laughed, wetly, and wiped her face with the back of her wrist.

They moved the urn to the head table, on a cloth they bought from the gift shop in the hotel lobby, and placed the sorbet, which had survived after all, in ice from the bar. The reception started forty minutes late. Nobody noticed the cake was cut at the wrong angle, or that the quartet had to repeat the second movement twice, or that the table with the urn carried a faint, unmistakable scent of wet bronze and roses.

Later, during the toasts, Pilar stood up and said her sister had always believed a wedding was a kind of weather, something you could not control but could dress for. Everyone laughed, and then everyone was quiet, and in the quiet Marisol, standing at the back with her shoes in her hand, thought that the freezer had done them a favor. Nothing had gone according to plan, and somehow the thing everyone would remember was the grandmother, dripping and dignified, arriving at her granddaughter's wedding on a dish towel.
```

**Bohemian**

```text
The cake arrived at the reception hall in three pieces, and nobody could agree on which piece was the top.

Marisol stood by the coat rack holding her phone, pretending to read messages from her mother. The bakery had called twice. The second time, a man named Dennis had said "structural incident" in the same voice you'd use for a flat tire, and then he'd asked if they wanted the bottom tier delivered separately, since it was still standing.

"It's fine," her cousin Ray said, arriving at her elbow with two glasses of something amber. "Nobody eats the cake. They come for the open bar and the ten minutes of dancing."

"I'm eating the cake."

"You're not even allowed to eat the cake. You're the bride."

"I'm the bride," Marisol said, "and I've been the bride for six hours, and I've been on my feet since five, and I have not once been allowed to sit in a chair that someone else didn't first check for bees."

Ray laughed. He had always laughed at the right moment, which was why she'd asked him to give the toast, and why she'd been regretting it since Tuesday.

The problem with the wedding, if you asked the guests, was the weather, which had been perfect. The problem, if you asked Marisol, was the ring. Theo had lost it somewhere between the vows and the first dance, and for twenty minutes the whole party had combed the lawn on their hands and knees, holding phone flashlights under the string lights. Her aunt had found a bobby pin. Someone's grandfather had found a quarter from 1971. Theo had found nothing, and had come back to the head table looking so stricken that Marisol had nearly laughed.

"It was in my pocket," he kept saying. "I had it in my pocket."

"Maybe you didn't."

"I put it in my pocket, Mari."

Then the flower girl, who was four, climbed onto the bottom tier of the cake that was still standing and announced that she was a lighthouse. Dennis was not there to stop her. Nobody was there to stop her except the uncle who had been holding a plate of shrimp, and by the time he set it down, the lighthouse had collapsed into frosting and the little girl was laughing so hard she could not breathe.

Marisol watched all of it from the doorway, and something in her chest let go, like a knot working loose.

She walked out onto the lawn, where the grass was wet and her shoes sank a little. The sky was going the particular purple it goes before it decides to be night. Behind her, the band started up again, a fraction off-key, and a cheer went up from inside.

Theo came out after a minute. He had his hands in his pockets, a habit that drove her crazy and that she had decided, somewhere around the second year of dating, to love.

"Found it," he said.

"Where?"

He pulled his hand out. The ring sat on his palm, dull under the lights, and beside it lay a crumpled napkin with the bakery's logo on it, which he must have used to wipe his fingers and then forgotten.

"It was in the napkin," he said. "I'd put it in the napkin. In my pocket. The napkin was in my pocket."

"You are a disaster."

"You married me anyway."

"I'm still deciding."

He held the ring out. She didn't take it right away. Behind them, through the open doors, she could hear Ray tapping a spoon against his glass, calling everyone to attention for the toast he'd been practicing in the car.

"The cake's in three pieces," she said.

"I know."

"Your niece ate the lighthouse."

"I heard."

"Nobody's going to remember the vows."

"I remember the vows," Theo said. "You said you'd keep the good spoons, even the ones with the chipped handles, because they were from your grandmother and you didn't care what anyone else thought about them."

She had said that. She had forgotten she'd said it.

Marisol took the ring, slid it on, and felt the small weight settle where it belonged. Then she took his hand, and they walked back inland together, toward the light and the noise and the three pieces of cake, which no one, it turned out, had any intention of eating in order.
```

*Judges:* vs baseline: gemini-2.5-flash-lite: prefer=Bohemian; gpt-4o-mini: prefer=baseline. vs one-liner: gemini-2.5-flash-lite: prefer=oneliner; gpt-4o-mini: prefer=oneliner.

## rewrite-2

> Rewrite this 'About us' paragraph for a 12-person accounting software company so it sounds less generic. Keep it about the same length:
> 
> Our company is a leading provider of innovative solutions. We are passionate about delivering exceptional value to our customers through cutting-edge technology and a commitment to excellence. Contact us today to learn more.

### deepseek/deepseek-v4.1-flash

**Baseline**

```text
We’re a 12-person team building accounting software that actually fits the way small firms work. No bloated enterprise features, no offshore support queues — just practical tools made by people who talk to our customers every week. Want to see if we’re a fit? Get in touch.
```

**One-liner**

```text
We're twelve people who build accounting software—small enough that the person who answers your call probably wrote the code you're asking about. No layers of support tickets or sales scripts. We ship updates because accountants told us what was slowing them down, and we actually use the same ledger logic we sell. Curious how that works in practice? Reach out and talk to one of us.
```

**Bohemian**

```text
Twelve of us build accounting software. When you call, you reach the person who wrote the code you are asking about, and no one here is measured on how fast they get you off the line. Contact us to learn more.
```

*Judges:* vs baseline: gemini-2.5-flash-lite: prefer=baseline; gpt-4o-mini: prefer=baseline. vs one-liner: gemini-2.5-flash-lite: prefer=oneliner; gpt-4o-mini: prefer=oneliner.

### anthropic/claude-haiku-5.5

**Baseline**

```text
We're a team of 12 people who build accounting software for small businesses, and we answer our own support emails. Our goal is simple: make bookkeeping and tax prep less of a headache so owners can get back to running their companies. Talk to us anytime and you'll reach the people who wrote the code.
```

**One-liner**

```text
We're twelve people who got tired of accounting software that treats bookkeepers like an afterthought. Our small team builds tools for the folks who close the books at 11 p.m. on the last day of the month, and we talk to those users every week. Every feature we ship starts with a question we actually asked a customer. If you'd like to see what that looks like, send us a message and we'll show you the product, and maybe a few things we still need to fix.
```

**Bohemian**

```text
We build accounting software for small firms, and we are twelve people, so you will usually reach the person who wrote the feature you are asking about. Most of us have worked in a bookkeeper's back office, and we built the things we wished had existed there: reconciliation that catches the duplicate invoice before month-end, and a close checklist you can hand to a new hire on their first day. If something breaks at 4:55 on a Friday, write to support@ourcompany.example and a human who knows the code will reply.
```

*Judges:* vs baseline: gemini-2.5-flash-lite: prefer=Bohemian; gpt-4o-mini: prefer=Bohemian. vs one-liner: gemini-2.5-flash-lite: prefer=oneliner; gpt-4o-mini: prefer=oneliner.

## brainstorm-2

> Brainstorm 5 campaign concepts for a public library that wants more teenagers to visit. Number them, with two sentences each.

### deepseek/deepseek-v4.1-flash

**Baseline**

```text
1. **Level Up at the Library**: Turn a meeting room into a rotating teen gaming zone with consoles, PCs, and monthly esports tournaments. Promote it through schools and Discord so teens see the library as a free, social place to play and compete.

2. **Teen Creator Studio**: Offer a drop-in space with ring lights, microphones, editing software, and backdrops for TikTok, YouTube, and podcast projects. Host short workshops on filming, sound, and online safety to attract teens who want to make content, not just consume it.

3. **After-Hours Study & Chill**: Keep one floor open late on select weeknights for teens only, with quiet study tables, group work pods, snacks, and low-key music. Partner with local tutors and counselors to add free homework help and stress-management sessions.

4. **Fandom HQ**: Run monthly cosplay, anime, fanfiction, and K-pop events with costume contests, swap meets, and themed photo booths. Let teens help plan the events so the library feels like their clubhouse, not an adult-run program.

5. **Library Influencer Squad**: Recruit a teen advisory crew that earns volunteer hours by reviewing books, making short promo videos, and designing displays. Give them real input on events and social media so their friends see the library as a place where teen voices actually matter.
```

**One-liner**

```text
1. **Late-Night Study Café** — On Friday nights, the library turns its quiet reading room into a teen-only café with free hot chocolate, lo-fi playlists, and five-minute "study hack" demos on topics like beating procrastination. It gives teens a safe, social alternative to home or the mall without the pressure of a formal program.

2. **Teen Curator Program** — Teens apply to design one shelf or display case per month around a theme they choose, from graphic novels to true crime to local history. Their names and photos go on the display, turning the library into a space they visibly own.

3. **Library Horror Story Contest** — Teens submit short scary stories set in the library, and the winners get their tales read aloud by the drama club during a flashlight-lit after-hours tour. It links the library's physical space to creativity, and the scariest story wins a $50 gift card.

4. **Speed-Friending with Books** — Teens rotate every three minutes, pairing a book they love with a stranger, then switch partners. It's a low-stakes way to meet new people and discover new reads, with snacks and a "no small talk required" rule.

5. **Escape Room: The Library Lock-In** — Small teams race to solve a 45-minute puzzle using only library resources, like a hidden call number or a note tucked inside a reference book. The first team to "break out" gets a pizza party and bragging rights.
```

**Bohemian**

```text
1. **The Nothing Required Card**
A library card with one printed condition: it costs nothing, and it never asks you to buy anything to stay. Campaign line: "The last place in town you can sit for three hours without being a customer." Targets the actual reason teens avoid cafés, malls and arcades — the pressure to spend.

2. **Free Hour, No Receipt**
Ads built around a single contrast: everything else in your day is metered. Screen time, data, bus fare, the £4 you don't have. Here, the clock starts and nothing is charged for it. Deliberately the opposite of a "come read" pitch — the books are the quiet bonus, not the offer.

3. **The Building That Doesn't Know You**
Your feed knows what you paused on, your school knows your grades, your parents know your location. The library is the one place that keeps no record of what you looked at. Positioned as a privacy pitch, which is both true of public libraries and directly interesting to this age group.

4. **Two Hours Before Anyone Notices**
Instead of advertising the library, advertise the gap: the stretch after school before anyone expects you home. Teens don't need a destination, they need a place to land, and the library is already open, already warm, already free. Posters placed at bus stops and school gates, timed to 3:15pm.

5. **What the Librarians Won't Tell You**
A mild anti-pitch that treats the teen as smarter than the marketing: instead of listing what's on offer, list what isn't advertised — the heated table by the window, the extension leads nobody mentions, the fact you can sit on the floor, the specific shelf where the good graphic novels are. Leans on the real, unglamorous truth that a library's best features are word-of-mouth, not brochure.

Recommendation: **3**. It's the only one that gives the library something no competitor can claim — not atmosphere (a café has that) and not warmth (a mall has that), but the absence of surveillance — and it lands on a subject this generation already argues about unprompted.
```

*Judges:* vs baseline: gemini-2.5-flash-lite: prefer=Bohemian; gpt-4o-mini: prefer=Bohemian. vs one-liner: gemini-2.5-flash-lite: prefer=Bohemian; gpt-4o-mini: prefer=Bohemian.

### anthropic/claude-haiku-5.5

**Baseline**

```text
1. **Library After Dark Gaming Nights:** Host monthly late-evening gaming tournaments in the library's community room, with console and tabletop options, free snacks, and a sign-up system run by teen volunteers. Teens get a safe, social space to hang out, and the event gives them a reason to discover the book collection while they wait for their next match.

2. **Teen-Curated Book Club & Playlist Series:** Invite teens to choose the monthly book selections, lead discussions, and pair each title with a playlist they build themselves, shared on the library's social channels. Giving teens real ownership over the collection makes the library feel like their space rather than an adult institution.

3. **Make-Your-Own Media Studio:** Open a bookable studio corner equipped with green screens, editing software, microphones, and a 3D printer, with workshops on podcasting, short films, and digital art. Teens who want to create things will find the library a place to build skills that matter for school and future careers.

4. **Paid Teen Volunteer & Job Shadow Program:** Offer a structured volunteer program where teens earn service hours, learn library work like cataloging and event planning, and receive a reference letter upon completion. The program builds real résumé experience and gives teens a reason to return every week.

5. **Library Lock-In Overnight Challenge:** Hold a once-a-season overnight event with escape rooms built from library materials, a movie night, a scavenger hunt through the stacks, and a supervised sleep-over area for registered teens. The novelty and sense of adventure create lasting memories that bring participants back for regular visits.
```

**One-liner**

```text
1. Overdue Confessions: Invite teens to anonymously submit the guilty secrets behind their library fines, such as the book they lost in a bathtub or the one they never meant to keep, and post the most entertaining ones on a wall in the teen section. Each confession earns a small fine forgiveness token, turning the library's most-resented policy into a reason to come in and read the stories.

2. The Rival Bookshelf: Set up a "shelf war" where two groups of teens each curate a shelf of books meant to convert the other side, with the library hosting a monthly reading debate to judge which shelf actually changed minds. Winners get to choose the next month's acquisitions, giving teens direct, visible power over what the collection contains.

3. Borrow a Stranger's Library Card: Let teens check out a sealed, mystery-wrapped book chosen by a local adult they've never met, with only a one-line description of the person's life, and then arrange a short conversation between the reader and the stranger afterward. The program turns a solitary borrowing habit into an unlikely intergenerational friendship that teens will talk about outside the building.

4. Tools Nobody Owns: Stock the library with things that are hard for teenagers to access elsewhere, like a sewing machine, a 3D printer, a sound booth, or a seed-saving kit, and let them check these out or book time slots alongside books. Many teens come for the gear first and discover the books while waiting, so the physical objects become the hook rather than the reading.

5. The Night Shift Archive: Run a monthly after-hours event where teens are locked in the library past closing with only a flashlight, a single old local-history archive box, and a prompt to dig up one forgotten fact about their own neighborhood to share at the end. It feels like a small adventure rather than a lesson, and the discoveries give teens a reason to return to the building and its records.
```

**Bohemian**

```text
1. **The Library Is the Only Place Nobody Is Selling You Anything.** A short poster series where ordinary places (the mall, the gaming café, the skate park) each carry a price tag, and the library's panel reads "Free, and no one is watching your wallet." It leans on the real fact that libraries cost nothing to enter, and on teenagers' sharp sense of being marketed to.

2. **Bring a Question You're Embarrassed to Ask.** Teens leave anonymous questions in a drop box at the library entrance, and staff answer them in a zine stocked on the shelves, with librarians finding the real answer through the library's databases. It grows from the fact that a library's core service is answering questions, and that teens are often too shy to ask one out loud.

3. **Overdue Notices, Reimagined as Fan Mail.** Teens who have ever kept a library book past its due date get a cheerful "We miss you" card, written by the branch's longest-serving staff member, that invites them back for a sequel: a themed book club for whatever they were reading. It uses the library's own overdue system as the hook, turning a small guilty moment into a warm welcome.

4. **The Quietest Room Is the Loudest Invitation.** A campaign built around the library's study rooms and quiet corners, promoted as places to be alone with your music, your thoughts or your group chat without an adult hovering nearby. It targets teenagers' need for private space at home and school, showing the library as a place to be unsupervised but safe.

5. **Make the Next Book Someone Else's Choice.** Teens pick a book for a stranger their own age and wrap it with a handwritten note, and the library shelves these "blind dates with a book" for the next teen to borrow. It grows from the idea that recommendations are a social act teens already do with friends, and gives them a reason to come in and be seen as someone with taste.
```

*Judges:* vs baseline: gemini-2.5-flash-lite: prefer=Bohemian; gpt-4o-mini: prefer=Bohemian. vs one-liner: gemini-2.5-flash-lite: prefer=oneliner; gpt-4o-mini: prefer=oneliner.

# Failure case

The task with the lowest combined `prefer` + `task` win rate against baseline on the test split in run `v3` (from `eval/results/v3/report_bohemian_test.md`, section 6). The judges preferred baseline on every comparison here.

## fiction-5

> Write the opening paragraph of a novel about a family-run hardware store that is about to close.

### deepseek/deepseek-v4.1-flash

**Baseline**

```text
The bell above the door of Fuller & Sons Hardware had been ringing for ninety-three years, a thin, tinny chime that had once announced farmers, newlyweds, and children clutching pennies for licorice, but on this particular Tuesday in late October it rang only for the wind, which slipped in every time the latch failed to catch and carried with it the smell of rain and the faint, sweet rot of leaves. Inside, the light fell in dusty columns across bins of nails sorted by size, coils of rope gone stiff with age, and a wall of paint cans whose labels had faded to pastel ghosts. Behind the counter, Walter Fuller ran his thumb along a crack in the oak that his grandfather had planed by hand, and he did not look up when his daughter placed the laminated sign in the window—EVERYTHING MUST GO—because he already knew the shape of those letters, had seen them in his dreams for months, and because looking at them would mean admitting that the store, like the town, like the family name itself, had finally run out of things to hold together.
```

**One-liner**

```text
The key broke on a Tuesday, and Maggie chose to read it as a sign rather than a nuisance. Thirty years of turning the same lock had worn the brass into something soft and knuckled, and now it lay in two pieces on the floor of Hargrove Hardware like a small, unhelpful wishbone. Outside, the town of Alder Creek was already lined up in cars at the new home improvement superstore on the bypass, buying faucets with names like *Vessel* and *Aurora*. Inside, her father was still straightening the bin of loose nails, one by one, though he had not spoken to a customer since the year turned.
```

**Bohemian**

```text
The loose screws had always been the store's real business, one and two at a time, a nickel apiece, and now we were pricing them to leave in lots, fifty cents a scoop, because nobody was going to stand there counting out a quarter's worth of galvanized wood screws after the sign went up. My mother sorted them by hand anyway, the way she had sorted them the first time, forty years ago, into the coffee cans she had labeled with a marker that was finally running dry. Everything in the store had a place and the place was about to become a room. Uncle Ray sat on the stool by the key machine with his coffee and his ledger, cutting a spare key for a man who had moved out of the neighborhood in 1998 and had driven back to say something he could not quite say, so instead he stood at the counter and watched Ray work the brass against the grinder, and the sparks fell in the little tray, and nobody mentioned the closing because the closing was not happening today.
```

*Judges:* vs baseline: gemini-2.5-flash-lite: prefer=baseline; gpt-4o-mini: prefer=baseline. vs one-liner: gemini-2.5-flash-lite: prefer=Bohemian; gpt-4o-mini: prefer=Bohemian.

### anthropic/claude-haiku-5.5

**Baseline**

```text
The last thing Walt Kowalczyk did before locking up the store for the final time was check the nail bins, the way his father had done every evening for forty-one years. He ran his palm along the rows of drywall screws and carriage bolts, feeling for the loose ones that wandered out of their trays and had to be coaxed home. There were fewer of them now. The shelves that once groaned under paint cans, garden hoses, and cases of copper elbows had been stripped bare over the past three months, leaving pale rectangles on the wood where the stock had sat so long it had kept the color out. Outside, the November wind pushed a plastic bag against the front window, and the sign above the door, HALLORAN & SONS HARDWARE, buzzed its tired single bulb into the dark. Walt pulled the chain on the last overhead light, stood a moment in the sudden gloom that smelled of linseed oil and cut keys, and wondered, not for the first time, which of the many things he had been meaning to say to his daughter he was now too late to say at all.
```

**One-liner**

```text
The last thing my father did before the lease ran out was count the keys. Not the ones in the bins, which we had already sold or boxed or given to the man from the consignment shop, but the blanks still hanging on the pegboard behind the register, the ones shaped for locks nobody made anymore: a Yale with a notched shoulder, a tubular key for a bicycle chain factory that had shut in 1979, a brass thing with three teeth like a tiny rake. He ran his thumb along each one, lips moving, and wrote the number on the back of an invoice. Two hundred and eleven. He said it the way a man reads a temperature. Then he tore the invoice in half, put one piece in his shirt pocket, and handed me the other, which is how I learned that the store was closing not because it had failed but because someone had finally offered enough money for the ground it sat on, and because the ground, as my father put it, had been waiting longer than any of us had.
```

**Bohemian**

```text
The last thing Walter Oduya sold from the hardware store on Carrow Street was a single brass hinge, two inches, for a cabinet door in the house across the road, the one with the blue shutters that his father had always said would fall off before the paint did. The woman who bought it paid in exact change she had counted out in her palm, and she asked whether the store was really closing, and Walter said yes, the twenty-ninth, and she nodded like someone who had already been told and had hoped the person telling her would turn out to be wrong.
```

*Judges:* vs baseline: gemini-2.5-flash-lite: prefer=baseline; gpt-4o-mini: prefer=baseline. vs one-liner: gemini-2.5-flash-lite: prefer=oneliner; gpt-4o-mini: prefer=oneliner.

