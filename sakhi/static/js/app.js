const $=id=>document.getElementById(id);
const DAY=864e5;
function arc(a,b,total,col){const r=80,C=2*Math.PI*r,len=(b-a)/total*C;
return `<circle cx="100" cy="100" r="${r}" fill="none" stroke="${col}" stroke-width="20" stroke-dasharray="${len} ${C-len}" transform="rotate(${a/total*360-90} 100 100)"/>`}
function fmt(d){return d.toLocaleDateString(undefined,{day:"numeric",month:"short",year:"numeric"})}
function drawRing(day,cyc,plen){
 const ov=cyc-14;
 let s=arc(0,plen,cyc,"var(--menses)")+arc(plen,ov-5,cyc,"var(--follic)")+arc(ov-5,ov+1,cyc,"var(--ovul)")+arc(ov+1,cyc,cyc,"var(--lut)");
 if(day!=null){const t=Math.min(day,cyc)/cyc*2*Math.PI-Math.PI/2;
 s+=`<circle cx="${100+80*Math.cos(t)}" cy="${100+80*Math.sin(t)}" r="9" fill="var(--surface)" stroke="var(--plum)" stroke-width="4"/>`}
 $("ring").innerHTML=s}
function run(save){
 const v=$("last").value,cyc=+$("cyc").value,plen=+$("plen").value;
 if(!v||!cyc){$("result").innerHTML='<p class="doc">Please choose the date your last period started.</p>';return}
 const last=new Date(v+"T00:00:00"),today=new Date();today.setHours(0,0,0,0);
 const day=Math.floor((today-last)/DAY)+1,next=new Date(last.getTime()+cyc*DAY);
 const ov=new Date(last.getTime()+(cyc-14)*DAY),f1=new Date(ov.getTime()-4*DAY),f2=new Date(ov.getTime()+DAY);
 const late=Math.floor((today-next)/DAY);
 let phase="";
 if(day<1)phase="Your last period date is in the future.";
 else if(day<=plen)phase="Period phase";
 else if(day<cyc-17)phase="Follicular phase";
 else if(day<=cyc-12)phase="Fertile window";
 else if(day<=cyc)phase="Luteal phase";
 drawRing(day>=1?day:null,cyc,plen);
 $("ringTxt").textContent=day>=1&&day<=cyc?`Day ${day}: ${phase}`:(late>0?"Period is late":phase);
 let h=`<p><b>Next period:</b> ${fmt(next)}<br><b>Fertile window:</b> ${fmt(f1)} to ${fmt(f2)}<br><b>Estimated ovulation:</b> ${fmt(ov)}</p>`;
 if(cyc<21||cyc>35)h+=`<div class="note">A cycle length of ${cyc} days is outside the usual 21 to 35 days. Consider a check-up.</div>`;
 if(late>=7)h+=`<div class="note alert">Your period looks ${late} days late. If you may be pregnant, take a test. If this happens often, see a gynecologist.</div>`;
 else if(late>0)h+=`<div class="note">Your period is ${late} day${late>1?"s":""} late. A small delay is common with stress or travel.</div>`;
 h+='<p class="doc" style="margin-top:12px">Predictions are estimates, and are not a form of birth control.</p>';
 $("result").innerHTML=h;
 if(save)try{localStorage.setItem("cc",JSON.stringify({v,cyc,plen}))}catch(e){}
}
$("go").onclick=()=>run(true);
try{const s=JSON.parse(localStorage.getItem("cc")||"null");if(s){$("last").value=s.v;$("cyc").value=s.cyc;$("plen").value=s.plen;run(false)}else drawRing(null,28,5)}catch(e){drawRing(null,28,5)}

$("bmiGo").onclick=()=>{const h=+$("h").value/100,w=+$("w").value;
 if(!h||!w){$("bmiOut").textContent="Enter your height and weight.";return}
 const b=w/(h*h);let c=b<18.5?"underweight range":b<23?"healthy range":b<25?"overweight risk range":"overweight range";
 $("bmiOut").textContent=`BMI ${b.toFixed(1)}: ${c}. Healthy weight for your height is about ${(18.5*h*h).toFixed(0)} to ${(22.9*h*h).toFixed(0)} kg.`};

const D={
pcodv:[["Early morning","Warm water with soaked methi seeds, or cinnamon water"],["Breakfast","Moong dal chilla with mint chutney, or vegetable oats upma"],["Mid-morning","1 fruit (apple, guava or berries) and a handful of nuts"],["Lunch","2 multigrain rotis, dal, large salad, sabzi, a bowl of curd"],["Evening","Roasted chana, or buttermilk with a sprouts salad"],["Dinner","Paneer or tofu bhurji with sautéed vegetables, 1 roti, soup"]],
pcodn:[["Early morning","Warm water with lemon, or cinnamon water"],["Breakfast","2-egg vegetable omelette with 1 multigrain toast"],["Mid-morning","1 fruit and 5 to 6 almonds"],["Lunch","Brown rice or 2 rotis, fish curry or dal, salad, sabzi"],["Evening","Roasted makhana or sprouts chaat, green tea"],["Dinner","Grilled chicken or fish with stir-fried vegetables, clear soup"]],
phase:[["Period (days 1 to 5)","Iron and warmth: spinach, beetroot, dates, jaggery in small amounts, lentils, ragi. Pair with vitamin C such as lemon. Drink plenty of fluids."],["Follicular","Fresh and light: sprouts, fruit, salads, flaxseeds, curd, whole grains."],["Ovulation","Fibre and antioxidants: leafy greens, berries, tomatoes, pulses, nuts and seeds."],["Luteal (before period)","Magnesium and calm: pumpkin seeds, banana, dark chocolate (small piece), oats. Cut back salt and caffeine to reduce bloating."]]};
function showDiet(k){$("dietTbl").innerHTML=D[k].map(r=>`<tr><th scope="row">${r[0]}</th><td>${r[1]}</td></tr>`).join("");
 document.querySelectorAll(".tabs button").forEach(b=>b.setAttribute("aria-pressed",b.dataset.d===k))}
document.querySelectorAll(".tabs button").forEach(b=>b.onclick=()=>showDiet(b.dataset.d));
showDiet("pcodv");

let hist=[],busy=false;
function add(role,t){const d=document.createElement("div");d.className="m "+role;d.textContent=t;$("chat").appendChild(d);$("chat").scrollTop=$("chat").scrollHeight;return d}
async function ask(q){
 q=(q||"").trim();if(busy||!q)return;busy=true;$("cq").value="";$("send").disabled=true;
 add("u",q);hist.push({role:"user",content:q});
 const el=add("b","Thinking…");
 try{
  const res=await fetch("/api/chat",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({messages:hist.slice(-10)})});
  const data=await res.json();
  if(!res.ok){hist.pop();el.textContent=data.error||"Sorry, something went wrong. Please try again.";return}
  const r={text:data.reply};
  el.textContent=r.text;hist.push({role:"assistant",content:r.text});
  }catch(err){
  hist.pop();
  el.textContent="Sorry, I could not reach the server. Please try again.";
 }finally{busy=false;$("send").disabled=false}
}
$("send").onclick=()=>ask($("cq").value);
$("cq").addEventListener("keydown",e=>{if(e.key==="Enter")ask($("cq").value)});
document.querySelectorAll(".chips button").forEach(b=>b.onclick=()=>ask(b.textContent));
