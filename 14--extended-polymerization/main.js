inp = `
BCHCKFFHSKPBSNVVKVSK

OV -> V
CO -> V
CS -> O
NP -> H
HH -> P
KO -> F
VO -> B
SP -> O
CB -> N
SB -> F
CF -> S
KS -> P
OH -> H
NN -> O
SF -> K
FH -> F
VV -> B
VH -> O
BV -> V
KF -> K
CC -> F
NF -> H
VS -> O
SK -> K
HV -> O
CK -> K
VP -> F
HP -> S
CN -> K
OB -> H
NS -> F
PS -> S
KB -> S
VF -> S
FP -> H
BB -> N
HF -> V
CH -> N
BH -> F
KK -> B
OO -> N
NO -> K
BP -> K
KH -> P
KN -> P
OF -> B
VC -> F
NK -> F
ON -> O
OC -> P
VK -> O
SH -> C
NH -> C
FB -> B
FC -> K
OP -> O
PV -> V
BN -> V
PC -> K
PK -> S
FF -> C
SV -> S
HK -> H
NB -> C
OK -> C
PH -> B
SO -> O
PP -> F
KV -> V
FO -> B
FN -> H
HN -> C
VB -> K
CV -> O
BC -> C
CP -> S
FS -> S
KP -> V
BS -> V
BK -> B
PN -> C
PF -> S
HO -> V
NC -> N
SS -> N
BO -> P
BF -> N
NV -> P
PB -> K
HB -> H
VN -> H
FV -> B
FK -> K
PO -> S
SC -> S
HS -> S
KC -> F
HC -> S
OS -> K
SN -> N
`

// inp = `NNCB
//
// CH -> B
// HH -> N
// CB -> H
// NH -> C
// HB -> C
// HC -> B
// HN -> C
// NN -> C
// BH -> H
// NC -> B
// NB -> B
// BN -> B
// BB -> N
// BC -> B
// CC -> N
// CN -> C`

var [poly, rules] = inp.trim(). split ('\n\n');

rules=(Object.fromEntries(rules.trim().split('\n').map(s => s.split(' -> '))))

pairs = Array.from(poly).slice(1).map((x,i)=>[poly[i],x]. join (''))

const first = poly[0];
const last = poly.slice(-1);

var counts = {}
for (let item of pairs) {
  counts[item] = (counts[item]||0) + 1
  }


  function iterate(cs) {
    var ncs = {}
    for (let key in cs) {
      if (rules[key]){

        var a = key[0] + rules[key]
ncs[a] = (ncs[a]||0)+cs[key]
a=rules[key]+key[1]
ncs[a] = (ncs[a]||0)+cs[key]
      } else{

        ncs[key] = (ncs[key]||0)+cs[key]
        }
      }
      return ncs
    }


for (let i = 0; i < 40; i++) {
counts = iterate(counts);
}

let elementCounts = {};
Object.keys(counts).forEach(ab => {
  let [a, b] = ab;
  elementCounts[a] = (elementCounts[a] || 0) + counts[ab];
  elementCounts[b] = (elementCounts[b] || 0) + counts[ab];
});
elementCounts[first] = (elementCounts[first] || 0) + 1;
elementCounts[last] = (elementCounts[last] || 0) + 1;

elementCounts = Object.values(elementCounts).map(x => x / 2);
console.log(Math.max(...elementCounts) - Math.min(...elementCounts));
