#include <cstddef>
#include <iostream>
#include <vector>
#include <unordered_map>
#include <set>
#include <unordered_set>

using st = std::size_t;

st n, m, k;
std::unordered_map<st, std::unordered_set<st> > c;
std::unordered_map<st, st> g;
std::unordered_set<st> p;

st bfs(st a) {
  if(!p.count(a)) {
    return 0;
  }
  
  p.insert(a);
  
  st s = 0;
  if(a <= n) {
    s++;
  }
  
  for(auto b : c[a]) {
    if(!p.count(b)) {
      s += bfs(b);
    }
  }
  
  return s;
}

int main() {
  std::cin >> n >> m >> k;
  for(st i = 0; i < k; i++) {
    st a, b;
    std::cin >> a >> b;
    c[a].insert(b);
  }
  
  std::vector<st> keys;
  for(auto a : c) {
    keys.push_back(a.first);
  }
  for(st a : keys) {
    g.insert({a, bfs(a)});
    p.clear();
  }
  
  for(auto b : g) {
    std::cout << b.first << " " << b.second;
  }
}