const $ = (s) => document.querySelector(s);
const $$ = (s) => document.querySelectorAll(s);
const api = async (url, options={}) => {
  const r = await fetch(url, options);
  if (!r.ok) throw new Error(await r.text());
  return r.json();
};
const badge = (label) => `<span class="badge ${String(label).toLowerCase().replaceAll(' ','-')}">${label}</span>`;
const miniBar = (v) => `<div class="mini-bar"><div><span style="width:${v}%"></span></div><strong>${v}%</strong></div>`;

$$('.nav[data-view]').forEach(btn => btn.addEventListener('click', () => {
  $$('.nav[data-view]').forEach(x=>x.classList.remove('active'));
  btn.classList.add('active');
  $$('.view').forEach(v=>v.classList.remove('active-view'));
  $('#' + btn.dataset.view).classList.add('active-view');
}));

async function loadOverview(){
  const d = await api('/api/dashboard/overview');
  const cards = [
    ['Active users', d.active_users, 'Synthetic personas'],
    ['Onboarding', d.onboarding_pct+'%', 'Average progress'],
    ['Mastery', d.mastery_pct+'%', 'Evidence-based'],
    ['Adoption', d.adoption_pct+'%', 'Behavior signal'],
    ['Reusable assets', d.reusable_assets, d.in_review+' in review'],
    ['Integration health', Math.round((d.successful_events/d.total_events)*100)+'%', d.total_events+' events'],
  ];
  $('#kpi-grid').innerHTML = cards.map(c=>`<div class="kpi"><span>${c[0]}</span><strong>${c[1]}</strong><small>${c[2]}</small></div>`).join('');
}

async function loadUsers(){
  const users = await api('/api/users');
  $('#user-select').innerHTML = users.map(u=>`<option value="${u.id}">${u.name} — ${u.role}</option>`).join('');
  $('#user-select').addEventListener('change', e=>loadLearner(e.target.value));
  await loadLearner(users[0].id);
}

async function loadLearner(id){
  const [u,caps,path] = await Promise.all([
    api(`/api/users/${id}`), api(`/api/users/${id}/capabilities`), api(`/api/users/${id}/learning-path`)
  ]);
  const avg = Math.round(caps.reduce((a,c)=>a+c.mastery_pct,0)/caps.length);
  $('#learner-profile').innerHTML = `
    <div><span class="eyebrow">DEMO PERSONA</span><h2>${u.name}</h2><p>${u.role} · ${u.region} · Manager: ${u.manager}</p></div>
    <div class="profile-stat"><span>Onboarding</span><strong>${u.onboarding_pct}%</strong></div>
    <div class="profile-stat"><span>Capability mastery</span><strong>${avg}%</strong></div>
    <div class="profile-stat"><span>Adoption</span><strong>${u.adoption_pct}%</strong></div>`;
  $('#capability-list').innerHTML = caps.map(c=>`<div class="cap-row"><div class="cap-top"><div class="cap-name"><strong>${c.name}</strong><span>${c.category} · Target level ${c.target_level} · ${c.evidence_count} evidence events</span></div><div class="score">${c.mastery_pct}%</div></div><div class="bar"><span style="width:${c.mastery_pct}%"></span></div></div>`).join('');
  $('#learning-path').innerHTML = path.map(a=>`<div class="learning-row"><div class="learn-top"><div class="learn-title"><strong>${a.title}</strong><span>${a.asset_type} · ${a.capability}</span></div>${badge(a.learning_status)}</div><div class="badges">${badge('v'+a.version)}${a.score!==null?badge('Score '+a.score):''}${a.due_date?badge('Due '+a.due_date):''}</div></div>`).join('');
}

async function loadManager(){
  const rows = await api('/api/dashboard/manager');
  $('#manager-table').innerHTML = rows.map(r=>`<tr><td><strong>${r.name}</strong><br><span style="color:#617085">${r.region}</span></td><td>${r.role}</td><td>${miniBar(r.onboarding_pct)}</td><td>${miniBar(r.mastery_pct)}</td><td>${miniBar(r.adoption_pct)}</td><td>${badge(r.intervention_risk)}</td></tr>`).join('');
}

async function loadGovernance(){
  const rows = await api('/api/governance/assets');
  $('#governance-table').innerHTML = rows.map(r=>`<tr><td><strong>${r.title}</strong><br><span style="color:#617085">Reviewed ${r.last_reviewed}</span></td><td>${r.asset_type}</td><td>${r.capability}</td><td>${r.version}</td><td>${badge(r.status)}</td><td>${r.owner}</td><td>${r.reusable?'Yes':'No'}</td></tr>`).join('');
}

async function loadEvents(){
  const rows = await api('/api/integrations/events');
  $('#events-table').innerHTML = rows.map(r=>`<tr><td><strong>${r.event_type}</strong></td><td>${r.source}</td><td>${r.destination}</td><td>${badge(r.status)}</td><td>${r.occurred_at}</td><td><code>${r.correlation_id}</code></td></tr>`).join('');
}

Promise.all([loadOverview(), loadUsers(), loadManager(), loadGovernance(), loadEvents()]).catch(err=>{
  console.error(err); alert('Demo data could not be loaded. See console for details.');
});
